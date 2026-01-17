---
layout: page
title: Publications
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
            <p class="pub-meta">
              {% if entry.venue %}<span class="pub-meta-item">{{ entry.venue }}</span>{% endif %}
              {% if entry.publication_type %}<span class="pub-meta-item">{{ entry.publication_type }}</span>{% endif %}
              {% if entry.patent %}<span class="pub-meta-item">{{ entry.patent }}</span>{% endif %}
              {% if entry.publisher %}<span class="pub-meta-item">{{ entry.publisher }}</span>{% endif %}
              {% if entry.volume %}<span class="pub-meta-item">{{ entry.volume }}</span>{% endif %}
              {% if entry.pages %}<span class="pub-meta-item">{{ entry.pages }}</span>{% endif %}
              {% if entry.year %}<span class="pub-meta-item">{{ entry.year }}</span>{% endif %}
            </p>
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
