---
title: How Singleton pattern in Java
date: 2010-03-23 01:00
author: arul
category: Programming
tags: Design,pattern,java
slug: how-singleton-pattern-in-java
disqus_identifier: /2010/03/how-singleton-pattern-in-java.html
status: published
---

[![image0](http://3.bp.blogspot.com/_X5tq9y9xv2s/S6hhueEzyWI/AAAAAAAAANA/MAXSbAXOX1Q/s400/design-is-a-behaviour.jpg)](http://3.bp.blogspot.com/_X5tq9y9xv2s/S6hhueEzyWI/AAAAAAAAANA/MAXSbAXOX1Q/s1600-h/design-is-a-behaviour.jpg)

**What is singleton ..?**

> It is a Design pattern. At this time what is Design pattern ..? To
> find out the best way to do a thing apart from the various method.
> Documenting a solution for the common problems.

**The Rule for the Singleton are:**

> -   restrict the creating the object of the class
> -   only one object is created over the application
> -   If multiple thread accessed then thread safe

**How to restrict the creating object..?**

> Define the access modifier of the constructor be *Private* and add the
> *final* keyword to the class then only the class can\'t be extended.

**Then How to create a one instance and access ..?**

> Create a instance with in the same class and accessed using the static
> method.

*Here is the Example code:*

``` java
public final class SingletonExample {

  private static SingletonExample singleton = new SingletonExample();

  private SingletonExample() {
    // Write your Functionality Here
  }

  public static SingletonExample getInstance() {
    return singleton;
  }
}
```

Usage: save the below as Arul.java

``` java
class Foo {
  public static SingletonExample obj;
  public static void method() {
    obj = SingletonExample.getInstance();
  }
}

class Arul{
  public static void main(String arg[]) {
    SingletonExample obj = SingletonExample.getInstance();
    Foo.method();
    if (Foo.obj == obj) {
      System.out.println("Both the objects are same ");
    } else {
      System.out.println("Not the same ");
    }
  }
}
```

In the Both Foo and Arul class access the same instance.

<div class="separator" style="clear: both; text-align: center;">

[![image1](http://3.bp.blogspot.com/_X5tq9y9xv2s/TAUe3R-Ca0I/AAAAAAAAAWM/-9WSRFEh-bk/s320/java+compile.jpg)](http://3.bp.blogspot.com/_X5tq9y9xv2s/TAUe3R-Ca0I/AAAAAAAAAWM/-9WSRFEh-bk/s1600/java+compile.jpg)

</div>

For more :
<http://en.wikipedia.org/wiki/Design_pattern_%28computer_science%29>
