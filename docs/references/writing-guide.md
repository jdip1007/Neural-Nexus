---
title: Neural Nexus Writing Guide
created: 2026-07-18
updated: 2026-07-18
type: reference
domain: hermes
tags: [writing, documentation, guide, knowledge-base]
sources: []
confidence: high
status: active
reviewed: 2026-07-18
---

# Neural Nexus — Wiki Writing Guide

> How to write knowledge base pages that compound over time. This guide applies to all 6 content types.

## Core Principles

### 1. Pages are for synthesis, not storage
A raw source (article, video, chat) goes in `raw/`. A wiki page is **what you learned** from it — distilled, cross-referenced, and connected to what you already know. Don't copy-paste. Synthesize.

**Bad page** (storage):
> The article says that transformers use self-attention. Self-attention was introduced in 2017. The paper is called "Attention Is All You Need." [then 500 words of copied content]

**Good page** (synthesis):
> [neural-nexus](concepts/neural-nexus.md) relies on structured knowledge organization to process information efficiently, replacing the isolated storage of traditional wikis. This integration is why automation enhances knowledge management — see [setup-guide](references/setup-guide.md).

### 2. Atomic focus — one idea per page
Each page covers one concept, one entity, one finding. If a page tries to explain 5 things, it becomes unsearchable and unlinkable. Split it.

**Signal to split:** You can't write a one-sentence "Definition" without referencing 3 other things that each deserve their own page.

### 3. Link before you explain
If another page already explains something, link to it instead of re-explaining. This is the compounding effect — each page builds on the network.

**Bad:**
> Backpropagation is the algorithm used to train neural networks by computing gradients of the loss with respect to weights using chain rule...

**Good:**
> Training uses structured workflows to update knowledge.

### 4. Frontmatter is non-negotiable
Every page needs frontmatter. It powers search, filtering, staleness detection, and the tag index. A page without frontmatter is invisible to tooling.

### 5. Write for your future self
You'll read these pages months from now. Include enough context that future-you can understand without re-reading the source. But don't include so much that the page becomes a wall of text — 50-150 lines is the sweet spot.

---

## Frontmatter Cheat Sheet

```yaml
---
title: Human-Readable Title          # Required. Title case.
created: 2026-07-18                   # Required. ISO date.
updated: 2026-07-18                   # Required. Bump on every edit.
type: concept                         # Required. One of: concept, entity, idea, finding, reading, comparison
domain: ai                            # Required. One of: ai, biotech, finance, devops, psychology, general, hermes
tags: [architecture, training]        # Required. Must be in SCHEMA.md taxonomy.
sources: [raw/articles/source.md]     # Required for readings/findings. Raw source files this page draws from.
confidence: medium                    # Recommended. high / medium / low
status: draft                         # Recommended. draft / active / archived
reviewed: 2026-07-18                  # Recommended. Date of last truth/validity check. Lint flags stale reviews.
# contradictions: [other-page]        # Optional. Set when this page conflicts with another.
---
```

### Confidence levels
| Level | When to use |
|-------|-------------|
| `high` | Well-supported across 3+ independent sources. Consensus. |
| `medium` | Supported by 1-2 sources. Reasonable but not confirmed. |
| `low` | Single source, opinion, or speculation. Flagged for review. |

### Status lifecycle
```
draft → active → archived
```
- `draft`: New, unpolished, may have incomplete sections.
- `active`: Stable, reviewed, linked properly.
- `archived`: Superseded or no longer relevant. Move to `_archive/`.

### Review tracking
Every active page should have a `reviewed:` date in frontmatter — the last time you verified the page's content is still accurate. The lint enforces this:
- Active pages without `reviewed` → warning
- Pages where `updated` is newer than `reviewed` → warning (content changed since last review)
- Pages not reviewed in 180+ days → info

**Review process** (run every 6 months):
1. Re-read the page and its cited sources
2. Check if information is still current
3. Check for contradictions with newer pages
4. Update content if needed, bump `updated` date
5. Set `reviewed: YYYY-MM-DD`
6. If no longer accurate → `status: archived`

---

## Wikilink Conventions

### Basic syntax
```
[[page-name]]              → links to page-name.md (any directory)
[[page-name|display text]] → links with custom display text
[[page-name#Header]]       → links to a specific header on that page
```

### Rules

1. **Minimum 2 outbound wikilinks per page.** Isolated pages are invisible. Link to related concepts, entities, or readings.
2. **Link to pages that exist, not phantom pages.** If you write `[[future-page]]`, create it or the lint will flag it.
3. **Prefer short basenames.** `[neural-nexus](concepts/neural-nexus.md)` resolves even if the file is at `concepts/neural-nexus.md`.
4. **Use display text when the slug is ugly.** `[[gpu-scaling|GPU scaling trends]]` reads better.
5. **Link on first mention only.** Don't link the same term 5 times in one page.
6. **Don't link inside code blocks.** Wikilinks in code blocks are ignored by the parser.

### What to link
- ✅ Concepts mentioned in passing → `[[concept-page]]`
- ✅ Entities (people, orgs, tools) → `[[entity-page]]`
- ✅ Related findings or readings → `[[reading-page]]`
- ❌ External URLs (use standard Markdown links: `[text](https://...)`)
- ❌ Headers within the same page (use standard `[#header]` or `[#header|text]`)

---

## Content Type Guidelines

### Concept Pages (`concepts/`)

**Purpose:** Explain a technical concept, theory, or framework.

**Structure:**
1. **Definition** — 2-4 sentences, jargon-free, for a newcomer
2. **Core Mechanism** — How it works. Diagrams welcome (Mermaid).
3. **Key Components** — Break into subsections
4. **Why It Matters** — What problem it solves
5. **Current State** — Where it is today
6. **Open Questions** — What's unresolved
7. **Related Concepts** — 2+ wikilinks

**Threshold:** Create when a concept is explained in depth OR appears in 3+ sources.

**Common mistakes:**
- ❌ Copying a Wikipedia article. Synthesize from your sources.
- ❌ No definition — jumping straight into details.
- ❌ No "Current State" — concepts evolve. Where is this now?

**Example flow:**
```
Definition: "Self-attention is a mechanism that lets each position
in a sequence attend to all other positions, computing weighted
relationships."

Core Mechanism: [Mermaid diagram of Q/K/V]

Key Components:
  - Query, Key, Value projections
  - Scaled dot-product
  - Multi-head attention

Why It Matters: Parallelizable, replaced RNNs, enabled long-context

Current State: Flash Attention, sliding window, sparse attention variants

Open Questions: Optimal attention for 1M+ context?
```

### Entity Pages (`entities/`)

**Purpose:** Document a person, organization, tool, or project.

**Structure:**
1. **Overview** — One paragraph elevator pitch
2. **Key Facts** — Bullet list (founded, location, known for, role)
3. **Relationships** — Wikilinks to connected entities
4. **Timeline** — Optional, key milestones
5. **In This Wiki** — Which readings/findings reference this entity

**Threshold:** 2+ source mentions OR central to 1 source.

**Common mistakes:**
- ❌ Writing a biography. This is a knowledge base, not Wikipedia.
- ❌ No relationships section — entities are nodes in a network.
- ❌ Listing every fact. Include what matters for understanding the domain.

### Idea Pages (`ideas/`)

**Purpose:** Capture raw thoughts before they're developed.

**Structure:**
1. **Thought** — 1-3 sentences, don't overthink
2. **Context** — What prompted this?
3. **Why It's Interesting** — What could it lead to?
4. **Potential Next Steps** — Optional action items

**Threshold:** No minimum. Create for any thought worth keeping.

**Common mistakes:**
- ❌ Over-structuring. Ideas should be quick to capture.
- ❌ Polishing before capturing. Get it down first, refine later.
- ❌ Not linking to related concepts. Even raw ideas should connect.

**Tip:** Ideas are the seed. When an idea matures, it often becomes a finding or concept. Update the idea page to link to the mature page, or convert it.

### Finding Pages (`findings/`)

**Purpose:** A processed insight — what you concluded after analyzing sources.

**Structure:**
1. **Question** — Frame as a question
2. **Evidence** — Sources, observations, data (with provenance `^[raw/...]`)
3. **Analysis** — Reasoning chain connecting evidence
4. **Conclusion** — 1-3 sentences, the takeaway
5. **Limitations** — What could be wrong

**Threshold:** Create when processing reveals a novel insight.

**Common mistakes:**
- ❌ No evidence section. A finding without sources is an opinion.
- ❌ No limitations. Every finding has caveats. Acknowledge them.
- ❌ Conclusion buried in analysis. State it directly.

**Quality test:** If someone asked "how do you know?", can they trace from your conclusion back through evidence to raw sources?

### Reading Pages (`readings/`)

**Purpose:** Summary of a source (article, video, paper, book).

**Structure:**
1. **Source** — Metadata table (type, URL, author, date)
2. **TL;DR** — 2-3 sentence summary
3. **Key Points** — Numbered, 3-5 items
4. **Notable Quotes** — Only the best 1-3
5. **Detailed Notes** — By section/topic
6. **Entities/Concepts Mentioned** — Wikilinks
7. **My Takeaways** — Your interpretation, separate from author's

**Threshold:** One per ingested source — always create.

**Common mistakes:**
- ❌ Transcribing instead of summarizing. Distill.
- ❌ No TL;DR. Busy future-you needs the 10-second version.
- ❌ Mixing author's points with your interpretation. Keep them separate.

### Comparison Pages (`comparisons/`)

**Purpose:** Side-by-side analysis of 2+ items.

**Structure:**
1. **What's Being Compared** — Table with basic info
2. **Why Compare** — What decision does this inform?
3. **Comparison Matrix** — Table: dimensions × items × winner
4. **Detailed Analysis** — One subsection per dimension
5. **Context-Dependent Verdict** — Best by use case
6. **Summary** — 2-3 sentence TL;DR

**Threshold:** When comparing 2+ items.

**Common mistakes:**
- ❌ No "Why Compare" — without context, comparisons are academic.
- ❌ Declaring a single winner. Most things are context-dependent.
- ❌ No sources. Which readings informed this comparison?

---

## Provenance: Citing Sources

Citations are **mandatory** for all pages derived from external material. A wiki without sources is just opinion. The lint script enforces this — readings and findings without sources are errors; concepts/entities/comparisons without sources are warnings.

### Two citation mechanisms

**1. Frontmatter `sources:` field** — page-level bibliography

List all raw source files this page draws from:
```yaml
sources: [raw/articles/attention-is-all-you-need.md, raw/videos/karpathy-llm-wiki.md]
```

**2. Inline provenance markers** — paragraph-level attribution

When a specific paragraph's claims come from a source, mark it:
```markdown
Transformers replaced RNNs because of their parallelism and long-range
attention. ^[raw/articles/attention-is-all-you-need.md]

However, attention scales quadratically with sequence length, which
limits context windows. ^[raw/videos/flash-attention-explained.md]
```

This lets a reader trace each claim to the exact source without re-reading the whole file.

### Citation rules by content type

| Type | Frontmatter `sources:` | Inline `^[raw/...]` | Lint enforcement |
|------|----------------------|---------------------|------------------|
| **reading** | REQUIRED (it's a summary OF a source) | Recommended for specific quotes | Error if missing |
| **finding** | REQUIRED (evidence-based) | REQUIRED for each evidence point | Error if missing |
| **concept** | Required when derived from sources | Recommended for specific claims | Warning if missing |
| **entity** | Required when derived from sources | Recommended | Warning if missing |
| **comparison** | Required when comparing from sources | Recommended | Warning if missing |
| **idea** | Optional (original thought) | Optional | Not checked |

### When to use inline provenance
- ✅ Pages synthesizing 3+ sources (attribute each claim)
- ✅ Findings — every evidence bullet should cite its source
- ✅ Readings — cite the source itself in frontmatter, use inline for quotes
- ✅ Concepts — cite where definitions/claims originate
- ❌ Common knowledge within the domain ("transformers use attention")
- ❌ Your own analysis or synthesis (that's implied by authorship)

### Capturing external URLs

If a page references an external URL in prose, that URL should be **captured to `raw/`** and cited — not left as a bare link. Bare URLs decay (link rot), and the wiki loses the source if the URL goes down.

**Workflow:**
1. Page references `https://example.com/article`
2. Fetch the article → save to `raw/articles/example-article.md` (with raw frontmatter: source_url, ingested, sha256)
3. Replace bare URL in prose with inline citation: `^[raw/articles/example-article.md]`
4. Add to frontmatter: `sources: [raw/articles/example-article.md]`

**Exception:** URLs pointing to tools, documentation, or services (e.g., `https://docs.python.org/`) don't need capturing — they're references, not sources of knowledge claims.

### What the lint checks
1. **Missing sources** — readings/findings without any citations → error
2. **Missing sources** — concepts/entities/comparisons without citations → warning
3. **Orphan citations** — inline `^[raw/path]` pointing to a file that doesn't exist → warning
4. **Missing source files** — frontmatter `sources:` listing files that don't exist → warning
5. **Uncaptured URLs** — external URLs in prose with no corresponding raw source → info

---

## Writing Process

### When ingesting a new source

```
1. Capture raw source → raw/{articles,videos,chats}/
2. Create reading page from template → readings/
3. Extract entities mentioned → create/update entities/
4. Extract concepts explained → create/update concepts/
5. Note novel insights → create findings/
6. Cross-reference: link everything (min 2 per page)
7. Update index-catalog.md + log.md
```

### When updating an existing page

```
1. Read the existing page first
2. Add new information in the right section
3. Bump `updated:` date in frontmatter
4. If new info contradicts: note both, set contradictions field
5. Check that wikilinks still resolve
6. Append to log.md: ## [date] update | page-name
```

### When splitting a page

```
1. Identify the sub-topics (each should be atomic)
2. Create new pages for each sub-topic
3. Move content, add cross-links between new pages
4. Replace original page with a summary + links to new pages
   (or archive it if fully split)
5. Update all pages that linked to the original
6. Log the split
```

---

## Style Guide

### Voice
- **Direct and concise.** No filler. Every sentence carries information.
- **Second person is fine** ("you can use X to...") for tutorials/references.
- **Avoid hedging** unless genuinely uncertain. Use confidence field for uncertainty.

### Formatting
- **Tables** for structured comparisons, metadata, timelines.
- **Numbered lists** for sequential steps.
- **Bullet lists** for unordered items.
- **Bold** for key terms on first mention.
- **Code blocks** for commands, file paths, code.
- **Blockquotes** for source quotes.
- **Admonitions** for warnings, tips, notes:

```markdown
> [!warning] Stale content
> This page hasn't been updated since 2025. Verify before relying on.

> [!tip] Quick test
> Run `node scripts/lint-wiki.js` after changes.
```

### Naming
- **Filenames**: `lowercase-with-hyphens.md` — no spaces, no CamelCase
- **Titles**: `Human-Readable Title Case` — in frontmatter `title:` field
- **Slugs**: Match filename (without `.md`) — used in `[[wikilinks]]`

### Length
| Section | Target |
|---------|--------|
| Definition / TL;DR | 2-4 sentences |
| Key Points | 3-7 items |
| Total page | 50-150 lines |
| Split trigger | 200+ lines |

---

## Quality Checklist

Before saving any page:

- [ ] Frontmatter complete (title, created, updated, type, domain, tags)
- [ ] All tags exist in SCHEMA.md taxonomy
- [ ] Minimum 2 outbound `[[wikilinks]]`
- [ ] Wikilinks point to existing pages (or plan to create them)
- [ ] No copied content — synthesized in your own words
- [ ] Sources cited: `sources:` frontmatter field AND/OR inline `^[raw/...]` markers
- [ ] For readings: source file captured in `raw/` and listed in frontmatter
- [ ] For findings: every evidence point has an inline citation
- [ ] External URLs in prose are captured to `raw/` (not left as bare links)
- [ ] Confidence level set (if opinion-heavy or single-source)
- [ ] Page is under 200 lines (split if over)
- [ ] `updated:` date bumped if modifying existing page
- [ ] Page added to `index-catalog.md` (or run `generate-catalog.js`)

Run the lint to verify:
```bash
node scripts/lint-wiki.js
```

---

## Examples

### Good concept page (excerpt)

```markdown
---
title: Self-Attention
created: 2026-07-18
updated: 2026-07-18
type: concept
domain: ai
tags: [architecture, attention, nlp]
sources: [raw/articles/attention-is-all-you-need.md]
confidence: high
status: active
---

# Self-Attention

## Definition

Self-attention is a mechanism where each position in a sequence
computes a weighted representation of all other positions, allowing
the model to capture relationships regardless of distance. It's the
core innovation behind [neural-nexus](concepts/neural-nexus.md).

## Core Mechanism

For each position, three vectors are computed: Query (Q), Key (K),
and Value (V). Attention scores are the dot product of Q and K,
scaled by √d_k, then softmaxed:

\[\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\]

\`\`\`mermaid
graph LR
    Input --> Q[Query] & K[Key] & V[Value]
    Q --> Dot[QKᵀ / √d]
    K --> Dot
    Dot --> Soft[Softmax]
    Soft --> Mult[× V]
    V --> Mult
    Mult --> Output
\`\`\`

## Why It Matters

Unlike structured knowledge systems, traditional wikis process information linearly.
all positions in parallel. This is why GPU scaling accelerated
transformer training — see [[gpu-scaling]].

## Current State

Standard attention is O(n²) in sequence length. Variants like
[[flash-attention]] and sparse attention reduce this to near-linear.
```

### Good reading page (excerpt)

```markdown
---
title: "Attention Is All You Need — Reading Notes"
created: 2026-07-18
updated: 2026-07-18
type: reading
domain: ai
tags: [architecture, attention, research]
sources: [raw/articles/attention-is-all-you-need.md]
confidence: high
status: active
---

# Attention Is All You Need — Reading Notes

## Source

| Field | Value |
|-------|-------|
| Type | paper |
| URL | https://arxiv.org/abs/1706.03762 |
| Authors | Vaswani et al. (Google) |
| Published | 2017-06-12 |

## TL;DR

Introduced the Transformer architecture, replacing recurrence with
self-attention. Achieved SOTA on translation while being faster to
train due to parallelism.

## Key Points

1. Self-attention computes relationships between all positions simultaneously
2. Multi-head attention lets the model attend to different representation subspaces
3. Positional encoding injects sequence order information
4. Eliminates recurrence entirely — fully parallelizable
```

---

## Anti-Patterns

### The Storage Room
```
❌ A page that's a copy-paste of a source with no synthesis.
   Raw material belongs in raw/. Wiki pages are for processed knowledge.
```

### The Island
```
❌ A page with zero outbound wikilinks.
   It's invisible in the graph and unreachable from other pages.
   Minimum 2 links. Always.
```

### The Wall of Text
```
❌ A 300-line page with no headers, no structure, no links.
   Split it. Add headers. Link concepts.
```

### The Stub
```
❌ A page with just a title and "TODO: write this later."
   Either write it now or don't create it. Stubs pollute the graph.
   (Exception: the seed page during initial setup.)
```

### The Clone
```
❌ A page that duplicates an existing page under a different name.
   Always search index-catalog.md before creating.
   The lint script catches these if they have the same tags.
```

### The Phantom Linker
```
❌ A page full of [[links]] to pages that don't exist.
   Either create the target pages or remove the links.
   The lint script flags broken wikilinks.
```

## Related

- [neural-nexus](concepts/neural-nexus.md)
- [setup-guide](references/setup-guide.md)
