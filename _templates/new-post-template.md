<%*
  let title = await tp.system.prompt("Title", tp.file.title);
  slug = title.toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '-')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
  tR += "---"
%>
title: <%* tR += title %>
date: <% tp.date.now("yyyy-MM-DD HH:mm:ss") %>
author: arul
category: others
tags: others
slug: <% slug %>
disqus_identifier: <% slug %>
cover: default.png
color: gray
headline: <% title %>
status: draft
---
