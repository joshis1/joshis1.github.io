---
layout: page
body_class: home-page
description: Notes on technical leadership, Java, software design, Linux, and the systems behind reliable products.
---

<section class="hero-band">
  <div class="hero-copy">
    <p class="eyebrow">Leadership · Java · Engineering</p>
    <h1>Building teams<br>and <em>building things.</em></h1>
    <p class="hero-intro">I’m Shreyas Joshi. I write about the craft of technical leadership, Java and software design, and the Linux systems that make products work.</p>
    <div class="hero-actions">
      <a class="button button-dark" href="#latest-writing">Explore the writing <span aria-hidden="true">↓</span></a>
      <a class="text-link" href="{{ '/about.html' | relative_url }}">A little about me <span aria-hidden="true">→</span></a>
    </div>
  </div>
  <figure class="hero-image">
    <img src="{{ '/assets/img/AVNET_Zedboard.png' | relative_url }}" alt="Avnet MicroZed development board used in an embedded Linux project">
    <figcaption><span>From the lab</span> MicroZed, Yocto and a lot of learning by doing.</figcaption>
    <span class="image-index" aria-hidden="true">01 / FIELD NOTES</span>
  </figure>
</section>

<section class="topic-strip" aria-label="Writing themes">
  <span>Technical leadership</span><span>Java &amp; software design</span><span>Linux &amp; embedded systems</span><span>Learning in public</span>
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
    <div><p class="eyebrow">Before this notebook</p><h2>Earlier projects &amp; notes</h2><p>Some older resources from my previous site are still available in their original form.</p></div>
    <ul class="legacy-links">
      <li><a href="https://drive.google.com/open?id=1NjI3IGuAGdeRiD6xSvwTR7y8Eq3xrEfr">Raspberry Pi notes <span>↗</span></a></li>
      <li><a href="https://github.com/joshis1/C_Programming/tree/master/resources/SNMP/RaspberryPI_SNMP">Raspberry Pi project <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1N2sB2UvEKqfOreuga1n0HCcsKTcVLZPs">Design patterns <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1xZBa--b-3kIRY0E85uhdk0i95X5nyOmr">Qt <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1R0_TzEtW2moJpd5ZcmWh0Bc5Tz7ATEi9">Kernel <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1-ZXhIWRDghVJ1uS-VzbUo_Yym0rO_5YO">Linux <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=14zIvY7DtwHnhkg9FMWlfFw9OIvZFR5Fn">Operating systems <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1kmtx3HNGLbkLuUonHRa8RD9jpLPoD9Za">Data structures <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1aUPRVvmi2XqNbA-PAj4I_Q5YJg_TzksU">Embedded systems <span>↗</span></a></li>
      <li><a href="https://drive.google.com/open?id=1Ym3kJR8bQce_lOxzJvVRtKtnzbBHbKtk">Decoder image <span>↗</span></a></li>
    </ul>
  </div>
</section>
