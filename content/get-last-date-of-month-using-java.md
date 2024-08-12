---
title: Get last date of month using java
date:   2011-09-08 00:24
author: arul
category:   Programming
tags:   java
slug:   get-last-date-of-month-using-java
status:   published
disqus_identifier:    /2011/09/get-last-date-of-month-using-java.html
---

Using Calendar class in java you get everything. We can get the last
date of the month using that. Please have a look of this code snippest
to get last date of the passing month. Here is the full code [click
Here](http://www.arulraj.net/labs/java/misc/DateExample.java)

``` java
public static Date getLastDateOfMonth(int year, int month) {
  Calendar calendar = new GregorianCalendar(year, month,
  Calendar.DAY_OF_MONTH);
  calendar.set(Calendar.DAY_OF_MONTH,
  calendar.getActualMaximum(Calendar.DAY_OF_MONTH));
  return calendar.getTime();
}
```

1.  In the first line we are creating calendar object with year, month
    and day. In these parameters we can pass any int to that day, I
    passed 5 here.
2.  calendar.getActualMaximum(Calendar.DAY_OF_MONTH) its returns the
    maximum day of this month. For example it will return 31 for
    January.
3.  calendar.set() set that maimum day to that current month day.
    Finally you got the last date of the month.

Such as you can get the first date of this month using
getActualMinimum() fucntion. Anyway all month starts with 01 :)

Simple enum for month

``` java
enum Month {
  JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER;

  public String getDisplayName() {
    char[] charArray = name().toLowerCase().toCharArray();
    charArray[0] = Character.toUpperCase(charArray[0]);
    return new String(charArray);
  }

  public int getId() {
    return ordinal();
  }

  public String getValue() {
    return String.format("%02d", getId()+1);
  }
}
```

Sometimes you want to display month select box in jsp. At that time you
can use getDisplayName() and getValue() functions with in enum.

``` jsp
<select id="monthBox" name="monthBox" >
<c:forEach var="month" items="${monthList}" >
<option value="<c:out value="${month.value}" />"><c:out
  value="${month.displayName}" /></option>
</c:forEach>
</select>
```

Here the above code is in struts MVC. The monthList value is set from
ModelMap.

The console outputs for that java class

[![image0](http://1.bp.blogspot.com/-Zo6Oq2AU4B0/TmhcUceVZeI/AAAAAAAAAr0/Tk9I22jffIY/s1600/dateexample-console.PNG)](http://1.bp.blogspot.com/-Zo6Oq2AU4B0/TmhcUceVZeI/AAAAAAAAAr0/Tk9I22jffIY/s1600/dateexample-console.PNG)
