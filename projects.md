---
layout: page
title: Projects
---

<section>
  <h2>Projects</h2>
  {% for project in site.data.projects %}
    <div class="project-entry">
      <h3>
        {% if project.slug %}
          <a href="{{ "/projects/" | append: project.slug | append: "/" | relative_url }}">{{ project.name }}</a>
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

<p>Replace the project data in <code>_data/projects.yml</code>.</p>
