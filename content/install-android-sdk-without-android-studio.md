---
title: Install Android SDK Without Android Studio
date: 2024-08-18 10:57
author: arul
category: Android
tags: Mobile,Git-Bash,windows
slug: install-android-sdk-without-android-studio
status: published
disqus_identifier: install-android-sdk-without-android-studio
cover: assets/images/install-android-sdk-cover.png
headline: Install Android SDK without android Studio. In this article explain about how to build and android application using gradle command. To do that setup android sdk is required. Handled everything on Git Bash windows.
---
Recently I have found opensource [water reminder](https://github.com/KeyurDiwan/Water-Reminder) application. But they don't provide APK file in their releases. So I want to build the APK file from the source.

I don't want to install Android Studio. Just want to setup Android SDK and build using Gradle. If you have these kind of niche requirement then this article for you.

I am using GitBash on windows. The steps will work on other operating system as well with minor tweaks.
## 🥎Install SDK

```
mkdir -p $HOME/portable/android-sdk
```

Then Add the `ANDROID_SDK_ROOT` in `.bashrc`

```
tee -a ~/.bashrc <<"EOF"
export ANDROID_SDK_ROOT="$HOME/portable/android-sdk"
export PATH="$PATH:$ANDROID_SDK_ROOT/cmdline-tools/bin:$ANDROID_SDK_ROOT/platform-tools"
EOF
```

### Cmdline and Platform tools

Download the `cmdline-tools` and `platform-tools`. Then extract those inside the folder

```
curl -L https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip -o $HOME/portable/android-sdk/cmdlinetools-win.zip

curl -L https://dl.google.com/android/repository/platform-tools-latest-windows.zip -o $HOME/portable/android-sdk/platform-tools.zip
```

Extract

```
unzip $HOME/portable/android-sdk/cmdlinetools-win.zip -d $HOME/portable/android-sdk/
unzip $HOME/portable/android-sdk/platform-tools.zip -d $HOME/portable/android-sdk/
```

Install Android 30. This app requires this platform version.

```
cd $HOME/portable/android-sdk/
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --list
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --install "platforms;android-30"
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --install "build-tools;30.0.3"
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --list_installed
```

Now you have successfully installed Android SDK in your PC.

To Get the latest zip or file for other Operating Systems from here

To download [Command Line Tools Only](https://developer.android.com/studio/index.html#command-line-tools-only)

To download [Platform Tools](https://developer.android.com/tools/releases/platform-tools?hl=en#downloads)

If you want to uninstall particular version

```
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --uninstall "platforms;android-30"
./cmdline-tools/bin/sdkmanager --sdk_root=${PWD} --uninstall "build-tools;30.0.3"
```
## 🛠Build App

Now I just clone the above app. Then

```
gradle bundle
```

Then you can find the apk files in `Water-Reminder/app/build/outputs/apk/`
## 📱Connect Your Phone

In Your phone

* Settings → About Phone → Build number → Tab 7 times
* Then Setting → Developer Options → Enable USB debugging

Then connect your phone via USB

```
./platform-tools/adb devices -l
```

Now its should list your device.
## ⛓Install App

To install using adb

```
./platform-tools/adb install /path/of/app-debug.apk
```

To install using gradle

```
gradle installDebug
```
## 🐛Issues faced


### Try to build the app with android 31

Initially I tried with the platform version `android-31` since my mobile Android version is 12. You can find the mapping [here](https://en.wikipedia.org/wiki/Android_version_history)

Changed the compileSdkVersion, buildToolsVersion and targetSdkVersion in build.gradle

```
    compileSdkVersion 31
    buildToolsVersion "31.0.0"
    defaultConfig {
        applicationId "io.github.z3r0c00l_2k.aquadroid"
        minSdkVersion 21
        targetSdkVersion 31
```

While building the app with that version I got the following error.

```
Build-tool 31.0.0 is missing DX at android-sdk\build-tools\31.0.0\dx.bat
```

![[android-sdk-build-tool-31-error.png]]

The fix for this is

```
cd $HOME/portable/android-sdk/build-tools/31.0.0/
ln -s d8.bat dx.bat

cd $HOME/portable/android-sdk/build-tools/31.0.0/lib/
ln -s d8.jar dx.jar
```

After this `gradle build` got success.

Refer [Github issue](https://github.com/microsoft/appcenter/issues/2341#issuecomment-1314272461) . There is a issue in both 31 and 32 version of tools.
### Cannot install without signing

Initially try to install normal APK. Its not installed and got error. Debug build solves that problem

### Different Notification tone for this app

Since its a water reminder app. I want to send different notification sound for this. To do that.

Settings → Apps → All apps → Water Reminder

![[android-sdk-water-reminder-notification.png]]

Click on the Notification Channel. Then select the sound in that

![[android-sdk-water-reminder-notification-sound.png]]
