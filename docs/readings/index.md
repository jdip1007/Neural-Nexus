# Readings

## Overview

Readings are summaries and analyses of external content including books, papers, articles, videos, and other media. They capture the key insights and takeaways from consuming information.

## Browse Readings

{% for reading in readings %}
- [{{ reading.title }}]({{ reading.url }})
{% endfor %}

## Add Reading

To add a new reading, create a markdown file in the `readings/` directory following the [schema guidelines](../SCHEMA.md#readings).

## Reading Categories

- **Books**: Comprehensive book summaries and analyses
- **Papers**: Research papers and academic articles
- **Articles**: Blog posts, news articles, reports
- **Videos**: Video content summaries and transcripts
- **Podcasts**: Audio content summaries and key points

## Quality Standards

- Include proper citations and sources
- Provide original analysis, not just summaries
- Highlight key insights and takeaways
- Connect to related concepts and findings
- Include critical evaluation when appropriate

---

*Last updated: {{ now }}*