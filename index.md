---
layout: page
body_class: home-page
description: Shreyas Joshi’s personal notes on software design, system design, and software architecture.
---

<section class="hero-band">
  <div class="hero-copy">
    <p class="eyebrow">Software Design · System Design · Architecture</p>
    <h1>Exploring software.<br><em>Sharing what I learn.</em></h1>
    <p class="hero-intro">I’m Shreyas Joshi. This is my personal notebook on software design, system design, and software architecture—a place to collect project notes, useful ideas, and lessons along the way.</p>
    <div class="hero-actions">
      <a class="button button-dark" href="#latest-writing">Explore the writing <span aria-hidden="true">↓</span></a>
      <a class="text-link" href="{{ '/about.html' | relative_url }}">A little about me <span aria-hidden="true">→</span></a>
    </div>
  </div>
  <figure class="hero-image">
    <img src="{{ '/assets/img/Building_software.png' | relative_url }}" alt="Team Work">
    <figcaption><span>Building software,</span>  guiding people.</figcaption>
    <span class="image-index" aria-hidden="true">01 / FIELD NOTES</span>
  </figure>
</section>

<section class="topic-strip" aria-label="Writing themes">
  <span>Software Design</span><span>System Design</span><span>Software Architecture</span><span>Project Notes</span>
</section>

<section class="writing-section content-width" id="latest-writing">
  <div class="section-heading">
    <div><p class="eyebrow">The notebook</p><h2>Ideas from the work</h2></div>
    <a class="text-link" href="{{ '/categoryview/' | relative_url }}">Browse all topics <span aria-hidden="true">→</span></a>
  </div>
  <div class="post-grid">
    {% for post in site.posts %}
      <article class="post-card{% if forloop.first %} post-card-featured{% endif %}">
        <a class="card-link" href="{{ post.url | relative_url }}">
          <span class="card-category">{{ post.categories.first | replace: '_', ' ' }}</span>
          <h3>{{ post.title }}</h3>
          <p>{{ post.excerpt | strip_html | strip_newlines | truncate: 190 }}</p>
          <span class="card-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time><span aria-hidden="true">↗</span></span>
        </a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="archive-band">
  <div class="content-width archive-inner">
    <div><p class="eyebrow">Before this notebook</p><h2>Earlier projects &amp; notes</h2><p>Selected older open-source projects are linked below. Archived documents are not publicly linked until their content and sharing permissions have been reviewed.</p></div>
    <ul class="legacy-links">
      <li><a href="https://github.com/joshis1/C_Programming/tree/master/resources/SNMP/RaspberryPI_SNMP">Raspberry Pi project <span>↗</span></a></li>
    </ul>
  </div>
</section>
