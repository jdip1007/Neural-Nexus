# Findings

## Overview

Findings are processed insights and conclusions derived from research, analysis, or investigation. They represent the core knowledge outputs that have been synthesized and validated.

## Browse Findings

{% for finding in findings %}
- [{{ finding.title }}]({{ finding.url }})
{% endfor %}

## Add Finding

To add a new finding, create a markdown file in the `findings/` directory following the [schema guidelines](../SCHEMA.md#findings).

## Finding Characteristics

- **Evidence-based**: Supported by sources and data
- **Validated**: Reviewed and verified for accuracy
- **Synthesized**: Combines information from multiple sources
- **Actionable**: Provides clear insights or recommendations

## Quality Standards

- Must include proper citations to sources
- Should be specific and measurable where possible
- Include confidence levels or uncertainty indicators
- Link to related concepts and entities

---

*Last updated: {{ now }}*