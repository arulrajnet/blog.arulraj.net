---
title: Toggle copy email in jQuery
date: 2011-05-15 11:30
author: arul
category: Browser
tags: javascript
slug: toggle-copy-email-in-jquery
disqus_identifier: toggle_copy_email_in_jquery
status: published
---

In my current project jquery plays a main role. I done some small fixes
on the jquery script. At that time i learned something on jquery. Here I
am going to explain one of my jquery experience.

To prevent copy and email address from a text box. This is used in most
of the sign-up form.

Requirment:

-   Jquery 1.6
-   Jquery Validates plugin (optional)

Here I have used jquery validate plugin for validating email in the
form.

How to prevent copy and paste in a text input..?

``` javascript
$("#user.email").bind("cut copy paste", function(e) {
    e.preventDefault();
});
```

`e.preventDefault()` --- means its return false.

if you want to toggle use return statement.

return true --- means you are allowed to copy and paste content in the
text input

return false --- means its prevent copy and paste in the text input.

**Demo Form:**

<iframe src="http://files.arulraj.net/code/html/prevent_email_jquery.html" width="600" height="150">
</iframe>

For Toggling copy email depends upon the check box status the following
javascript is used in the above demo

``` javascript
$("#user.email").bind("cut copy paste", function(e) {
    //e.preventDefault();
    return $("div input[name='allow.copy']:checkbox").is(":checked");
    // false means not allow to copy.
});
```

For html code [Click
here](http://files.arulraj.net/code/html/prevent_email_jquery.html) and
view the source
