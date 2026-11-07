---
layout: page
title: Browse by topic
permalink: /categoryview/
description: Explore Shreyas Joshi's writing by topic.
---

<section class="archive-page content-width">
    <header class="page-heading">
        <p class="eyebrow">The archive</p>
        <h1>Browse by topic</h1>
        <p>Practical notes from software design, Java, Linux and embedded systems.</p>
    </header>
    {% assign categories = site.categories | sort %}
    <nav class="topic-index" aria-label="Topics">
        {% for category in categories %}
            <a href="#{{ category | first | slugify }}">{{ category[0] | replace: '_', ' ' }} <span>{{ category | last | size }}</span></a>
        {% endfor %}
    </nav>
    {% for category in categories %}
        <section class="archive-category" id="{{ category | first | slugify }}">
            {% assign category_posts = category | last %}
            {% assign category_count = category_posts | size %}
            <div class="archive-category-heading"><h2>{{ category[0] | replace: '_', ' ' }}</h2><span>{{ category_count }} {% if category_count == 1 %}article{% else %}articles{% endif %}</span></div>
            {% assign sorted_posts = site.posts | sort: 'title' %}
            <ul class="archive-list">
                {% for post in sorted_posts %}
                    {% if post.categories contains category[0] %}
                        <li><a href="{{ post.url | relative_url }}"><span class="archive-title">{{ post.title }}</span><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time></a><p>{{ post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p></li>
                    {% endif %}
                {% endfor %}
            </ul>
        </section>
    {% endfor %}
</section>
