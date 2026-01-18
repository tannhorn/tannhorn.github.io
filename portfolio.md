---
layout: page
title: Portfolio
---

<section>
  <h2>Portfolio</h2>
  {% for project in site.data.projects %}
    <div class="project-entry">
      <h3>
        {% if project.slug %}
          <a href="{{ "/portfolio/" | append: project.slug | append: "/" | relative_url }}">{{ project.name }}</a>
        {% else %}
          {{ project.name }}
        {% endif %}
      </h3>
      <p>{{ project.summary }}</p>
      <p>Status: {{ project.status }}</p>
      {% if project.link %}
        <p><a href="{{ project.link }}">Project link</a></p>
      {% endif %}
    </div>
  {% endfor %}
</section>

<p>Replace the portfolio data in <code>_data/projects.yml</code>.</p>
