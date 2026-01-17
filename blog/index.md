---
layout: page
title: Blog
---

<p>Subscribe via <a href="{{ "/feed.xml" | relative_url }}">RSS/Atom feed</a>.</p>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</span>
    </li>
  {% endfor %}
</ul>
