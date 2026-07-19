# Entities

## Overview

Entities are people, organizations, tools, projects, and other real-world objects or entities referenced in the knowledge base.

## Browse Entities

{% for entity in entities %}
- [{{ entity.title }}]({{ entity.url }})
{% endfor %}

## Add Entity

To add a new entity, create a markdown file in the `entities/` directory following the [schema guidelines](../SCHEMA.md#entities).

## Entity Categories

- **People**: Researchers, authors, contributors
- **Organizations**: Institutions, companies, labs
- **Tools**: Software, platforms, instruments
- **Projects**: Research projects, initiatives
- **Other**: Any other real-world entities

---

*Last updated: {{ now }}*