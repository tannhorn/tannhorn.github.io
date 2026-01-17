---
layout: page
title: Publications
---

<section>
  <h2>Selected Publications</h2>
  {% for pub in site.data.publications %}
    <div class="pub-entry">
      <h3>{{ pub.title }}</h3>
      <p>{{ pub.authors }}</p>
      <p>{{ pub.venue }} · {{ pub.year }}</p>
      {% if pub.link %}
        <p><a href="{{ pub.link }}">Link</a> · {{ pub.note }}</p>
      {% endif %}
    </div>
  {% endfor %}
</section>

<p>Replace the publication data in <code>_data/publications.yml</code>.</p>
