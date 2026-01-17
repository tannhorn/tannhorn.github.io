---
layout: page
title: CV
---

<section>
  <h2>Experience</h2>
  {% for entry in site.data.cv %}
    <div class="cv-entry">
      <h3>{{ entry.role }} | {{ entry.org }}</h3>
      <p>{{ entry.location }} · {{ entry.start }} - {{ entry.end }}</p>
      {% if entry.highlights %}
        <ul>
          {% for item in entry.highlights %}
            <li>{{ item }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    </div>
  {% endfor %}
</section>

<p>Replace the CV data in <code>_data/cv.yml</code>.</p>
