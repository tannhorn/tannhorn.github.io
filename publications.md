---
layout: page
title: Publications
pdf_link: /assets/publications.pdf
---

{% if site.data.publications.intro_md %}
  <div class="pub-intro">
    {{ site.data.publications.intro_md | markdownify }}
  </div>
{% endif %}

{% for section in site.data.publications.sections %}
  <section class="pub-section">
    <div class="pub-section__header">
      <h2>{{ section.title }}</h2>
    </div>
    <div class="pub-section__body">
      {% for entry in section.entries %}
        <div class="pub-entry{% if entry.highlight %} is-highlight{% endif %}">
          <div class="pub-entry__main">
            <h3 class="pub-title">{{ entry.title }}</h3>
            {% if entry.authors_md %}
              <div class="pub-authors">
                {{ entry.authors_md | markdownify }}
              </div>
            {% endif %}
            {% include pub_meta.html entry=entry %}
            {% if entry.note_md or entry.description_md or entry.credit_md %}
              <div class="pub-notes">
                {% if entry.note_md %}
                  {{ entry.note_md | markdownify }}
                {% endif %}
                {% if entry.description_md %}
                  {{ entry.description_md | markdownify }}
                {% endif %}
                {% if entry.credit_md %}
                  <div class="pub-credit">
                    {{ entry.credit_md | markdownify }}
                  </div>
                {% endif %}
              </div>
            {% endif %}
          </div>
          {% if entry.doi or entry.url %}
            <div class="pub-links">
              {% if entry.doi %}
                <a href="https://doi.org/{{ entry.doi }}" target="_blank" rel="noopener noreferrer" aria-label="DOI link for {{ entry.title | escape }} (opens in new tab)">DOI</a>
              {% endif %}
              {% if entry.url %}
                {% if entry.doi %} · {% endif %}
                <a href="{{ entry.url }}" target="_blank" rel="noopener noreferrer" aria-label="External link for {{ entry.title | escape }} (opens in new tab)">Link</a>
              {% endif %}
            </div>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </section>
{% endfor %}
