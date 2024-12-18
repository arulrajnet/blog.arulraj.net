---
title: How to copy commits from one branch to another in GIT
date: 2012-01-13 02:16:00
author: arul
category:   Programming
tags:   GIT, Linux
slug:   how-to-copy-commits-from-one-branch-to-another-in-git
status:   published
disqus_identifier:    /2012/01/how-to-copy-commits-from-one-branch-to-another-in-git.html
---

I have GIT version management tool for versioning and using gitolite for
user and project management within git. Will tell about this gitolite
story in a seperate post.

Here we are going to learn how to copy commits from your master to
branch.

Basically I am a linux enthusiast so I will explain everthing here in
commends. Feel free to use git commends 😄

-   First you have to check where you are now.

``` bash
git branch -a
```

That **\*** will where you are. Now I am in Master branch.

[![image0](http://4.bp.blogspot.com/-cOUKcHXwslk/Tw_aT7ePh7I/AAAAAAAAIy8/8XFZMPUOZhg/s400/git-branch.PNG)](http://4.bp.blogspot.com/-cOUKcHXwslk/Tw_aT7ePh7I/AAAAAAAAIy8/8XFZMPUOZhg/s1600/git-branch.PNG)
GIT Branch

-   Create a new branch and move to that created branch

``` bash
git branch <branch_name>
git checkout <branch_name>
```

If you are already created branch. No need create branch just git
checkout

-   Once again confirm Are you in correct branch.

``` bash
git branch -a
```

-   Pick up the commits to this branch

``` bash
git cherry-pick <first_some_character_of_commit_hash>
Ex: git cherry-pick d1c4b9a5a21e3d09cae
```

-   How to get the hash tag of commits

git log

[![image1](http://1.bp.blogspot.com/-2vSzYrj_sfk/Tw_nLsAJSGI/AAAAAAAAIzU/k_60_quiZbE/s400/git-log.PNG)](http://1.bp.blogspot.com/-2vSzYrj_sfk/Tw_nLsAJSGI/AAAAAAAAIzU/k_60_quiZbE/s1600/git-log.PNG)
GIT Log

You can get the has tag from here.

-   Then Switch back to master

``` bash
git checkout master
```

-   For push this branch to remote server

``` bash
git push origin <branch_name>
```

-   For delete the locally created branch

``` bash
git branch -D <branch_name>
```
