---
layout: page
title: Blog
---

<p>If I find the need to write something up, I will post it here. No guarantee of content, but you can still subscribe via <a href="{{ "/feed.xml" | relative_url }}">RSS/Atom feed</a>.</p>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</span>
    </li>
  {% endfor %}
</ul>
