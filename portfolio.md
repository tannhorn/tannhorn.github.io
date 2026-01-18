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
        <div class="project-entry">
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
          <p class="project-summary"><strong>Focus:</strong> {{ project.summary }}</p>
          {% if project.role or project.tools or project.outcome %}
            <dl class="project-meta">
              {% if project.role %}
                <div class="project-meta-row">
                  <dt>Role</dt>
                  <dd>{{ project.role }}</dd>
                </div>
              {% endif %}
              {% if project.tools %}
                <div class="project-meta-row">
                  <dt>Tools</dt>
                  <dd>{{ project.tools }}</dd>
                </div>
              {% endif %}
              {% if project.outcome %}
                <div class="project-meta-row">
                  <dt>Outcome</dt>
                  <dd>{{ project.outcome }}</dd>
                </div>
              {% endif %}
            </dl>
          {% endif %}
          {% if project.link %}
            <p class="project-links">
              <a href="{{ project.link }}" target="_blank" rel="noopener noreferrer" aria-label="Visit {{ project.name | escape }} website (opens in new tab)">External site</a>
            </p>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </section>
{% endfor %}
