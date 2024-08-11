<%*
  let title = await tp.system.prompt("Title", tp.file.title);
  slug = title.toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
  tR += "---"
%>
title: <%* tR += title %>
date: <% tp.date.now("yyyy-MM-DD HH:mm") %>
author: arul
category:
tags:
slug: <% slug %>
status: draft
---
