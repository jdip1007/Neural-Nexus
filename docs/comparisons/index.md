# Comparisons

## Overview

Comparisons are side-by-side analyses that evaluate and contrast different concepts, methods, tools, or approaches. They help in understanding relative strengths, weaknesses, and use cases.

## Browse Comparisons

{% for comparison in comparisons %}
- [{{ comparison.title }}]({{ comparison.url }})
{% endfor %}

## Add Comparison

To add a new comparison, create a markdown file in the `comparisons/` directory following the [schema guidelines](../SCHEMA.md#comparisons).

## Comparison Categories

- **Tools vs Tools**: Software, platforms, methodologies
- **Concepts vs Concepts**: Theoretical frameworks, approaches
- **Methods vs Methods**: Techniques, protocols, processes
- **Standards vs Standards**: Different approaches to same problem

## Comparison Framework

Each comparison should include:

- **Overview**: What is being compared and why
- **Criteria**: Evaluation dimensions and metrics
- **Analysis**: Detailed comparison on each criterion
- **Conclusions**: Key takeaways and recommendations
- **Sources**: Evidence supporting the comparison

## Best Practices

- Use objective criteria for evaluation
- Provide clear visual organization
- Include recent and relevant examples
- Highlight practical implications
- Maintain neutrality and avoid bias

---

*Last updated: {{ now }}*