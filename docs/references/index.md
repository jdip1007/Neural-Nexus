# References

## Overview

References are the source materials and citations that support the knowledge base content. They provide the foundation for all claims, findings, and analyses.

## Browse References

{% for reference in references %}
- [{{ reference.title }}]({{ reference.url }})
{% endfor %}

## Add Reference

To add a new reference, create a markdown file in the `references/` directory following the [schema guidelines](../SCHEMA.md#references).

## Reference Types

- **Academic Papers**: Peer-reviewed research articles
- **Books**: Published books and textbooks
- **Websites**: Online articles, blogs, documentation
- **Videos**: Video content from YouTube, conferences, etc.
- **Datasets**: Data sources and repositories
- **Tools**: Software and tools used in research

## Citation Standards

- Use consistent citation format across all references
- Include all necessary metadata (author, title, date, URL, etc.)
- Verify that all links are active and accessible
- Link to related readings and findings when applicable

---

*Last updated: {{ now }}*