---
title: Prompter4J Released 1.0
slug:   prompter4j-released-1-0
date:   2015-05-10 15:34:09
tags:   java, prompter4j
category:   Prompter4J
author: arul
lang:   en
disqus_identifier:    /2015/05/prompter4j-released-1-0.html
---

Prompter4J is a library to get the user raw input in an interactive
manner.

## Maven

Add this dependency in your pom.xml and start using.

``` xml
<dependency>
    <groupId>com.github.arulrajnet</groupId>
    <artifactId>prompter4j</artifactId>
    <version>1.0</version>
</dependency>
```

## Download JAR

<http://central.maven.org/maven2/com/github/arulrajnet/prompter4j/1.0/prompter4j-1.0.jar>

## How to Use

**Get an integer value**

``` java
int dd = Prompter.prompt(new PromptOptions("Enter your age :").
        required(Boolean.TRUE).type(Integer.class));
```

*The Output*

``` text
Enter your age :
> df
Give input as Integer
Enter your age :
> 12
```

**Choose a value from an array**

``` java
Integer[] levelArray = {3 ,4, 5};
Integer ee = Prompter.prompt(new PromptOptions("Select Any one :").
            choices(levelArray).required(true).type(Integer.class));
```

*The output*

``` text
Select Any one :
3
4
5
> 8
Select from choices
Select Any one :
3
4
5
> 5
```

**Choose a value from Enum**

``` java
enum DAY {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
DAY ff = Prompter.prompt(new PromptOptions("Select your day :").
        choices(DAY.class).defaultValue(DAY.SUNDAY.toString()).type(DAY.class));
```

*The Output*

``` text
Select your day : Default is SUNDAY
SUNDAY
MONDAY
TUESDAY
WEDNESDAY
THURSDAY
FRIDAY
SATURDAY
>
SUNDAY
```
