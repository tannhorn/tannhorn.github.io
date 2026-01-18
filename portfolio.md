---
layout: page
title: Portfolio
---

{% for category in site.data.portfolio %}
  <section class="cv-section">
    <div class="cv-section__header">
      <h2>{{ category.name }}</h2>
      {% if category.tagline %}
        <p class="cv-meta">{{ category.tagline }}</p>
      {% endif %}
    </div>
    <div class="cv-section__body">
      {% for project in category.items %}
        <div class="cv-entry">
          <div class="cv-entry__header">
            <h3 class="cv-entry__title">
              {% if project.slug %}
                <a href="{{ "/portfolio/" | append: project.slug | append: "/" | relative_url }}">{{ project.name }}</a>
              {% else %}
                {{ project.name }}
              {% endif %}
            </h3>
            <span class="cv-entry__meta">{{ project.status }}</span>
          </div>
          <p>{{ project.summary }}</p>
          {% if project.link %}
            <p>
              <a href="{{ project.link }}" target="_blank" rel="noopener noreferrer" aria-label="Visit {{ project.name | escape }} website (opens in new tab)">
                {{ project.name }} website
              </a>
            </p>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </section>
{% endfor %}
