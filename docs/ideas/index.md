# Ideas

## Overview

Ideas are raw thoughts, brainstorming concepts, speculative concepts, and early-stage hypotheses. They represent the creative and exploratory phase of knowledge development before formal analysis.

## Browse Ideas

{% for idea in ideas %}
- [{{ idea.title }}]({{ idea.url }})
{% endfor %}

## Add Idea

To add a new idea, create a markdown file in the `ideas/` directory following the [schema guidelines](../SCHEMA.md#ideas).

## Idea Categories

- **Brainstorming**: Raw thoughts and concepts
- **Hypotheses**: Testable propositions and predictions
- **Speculations**: Theoretical possibilities and explorations
- **Conceptual Frameworks**: Early-stage theoretical models
- **Innovations**: New approaches and methodologies

## Idea Development Process

1. **Capture**: Record the idea as-is without filtering
2. **Categorize**: Assign to appropriate category and tags
3. **Connect**: Link to related concepts and entities
4. **Develop**: Expand into more formal findings or concepts
5. **Validate**: Test and refine through research and analysis

## Quality Guidelines

- Preserve original thinking and creativity
- Include context and background when relevant
- Link to supporting evidence when available
- Mark confidence levels and uncertainty
- Track evolution from idea to validated concept

---

*Last updated: {{ now }}*