---
layout: page
title: CV
pdf_link: /assets/cv.pdf
---

{% for section in site.data.cv.sections %}
  <section class="cv-section">
    <div class="cv-section__header">
      <h2>{{ section.title }}</h2>
    </div>
    <div class="cv-section__body">
      {% if section.kind == "skills" %}
        {% for category in section.categories %}
          <div class="cv-entry">
            <h3 class="cv-entry__title">{{ category.name }}</h3>
            {% if category.items_list %}
              <p class="cv-meta">{{ category.items_list | join: ", " }}</p>
            {% endif %}
            {% if category.items_md %}
              <ul>
                {% for item in category.items_md %}
                  <li>{{ item | markdownify }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
        {% endfor %}
      {% elsif section.kind == "education" %}
        {% for entry in section.entries %}
          <div class="cv-entry">
            <h3 class="cv-entry__title">{{ entry.degree }} | {{ entry.institution }}</h3>
            <p class="cv-meta">{{ entry.location }} · {{ entry.dates }}</p>
            {% if entry.details_md %}
              <ul>
                {% for item in entry.details_md %}
                  <li>{{ item | markdownify }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
        {% endfor %}
      {% else %}
        {% for entry in section.entries %}
          <div class="cv-entry">
            <div class="cv-entry__header">
              <h3 class="cv-entry__title">{{ entry.org }}</h3>
              <span class="cv-entry__meta">{{ entry.location }}</span>
            </div>
            {% for role in entry.roles %}
              <div class="cv-role">
                <div class="cv-role__header">
                  <span class="cv-role__title">{{ role.title }}</span>
                  <span class="cv-role__dates">{{ role.dates }}</span>
                </div>
                {% if role.highlights_md %}
                  <ul>
                    {% for item in role.highlights_md %}
                      <li>{{ item | markdownify }}</li>
                    {% endfor %}
                  </ul>
                {% endif %}
              </div>
            {% endfor %}
          </div>
        {% endfor %}
      {% endif %}
    </div>
  </section>
{% endfor %}
