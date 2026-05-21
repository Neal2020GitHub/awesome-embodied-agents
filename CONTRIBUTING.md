# Contributing

Thanks for helping improve Awesome Embodied Agents.

## Scope

This repository focuses on embodied agents where VLMs or MLLMs serve as agentic components for perception, memory, reasoning, planning, exploration, navigation, interaction, or evaluation.

Good fits include:

- embodied memory and embodied RAG
- VLM/MLLM-based embodied planning and reasoning
- navigation agents with memory, reflection, or spatial reasoning
- embodied question answering agents
- manipulation agents using VLMs as planners, skill selectors, or tool users
- benchmarks for embodied agent capabilities

Usually out of scope:

- end-to-end VLA policies
- world models or video prediction methods
- diffusion policies
- low-level robot control
- generic LLM agents without embodied perception

Borderline works can be included if the contribution is agentic rather than only policy learning.

## Entry Format

Use this format in `README.md`:

```md
* [2026] Paper Title [[paper](URL)] [[project](URL)] [[code](URL)]
```

Use lowercase link labels: `paper`, `project`, `code`, `data`, `video`, or `blog`. If a link is unavailable, omit it rather than writing `TBD`.

Within each section, entries should be sorted by year in descending order. Do not add nested subsections inside a section; keep each section as a single chronological list.

## Metadata

`README.md` is the source of truth for the public awesome list. `papers.yaml` is optional structured metadata and may be updated when useful for maintenance scripts.

```yaml
- title: "Paper Title"
  year: 2026
  authors: "LastName et al."
  category: "Embodied Memory"
  tags:
    - memory
    - spatial reasoning
  task:
    - embodied exploration
  links:
    paper: ""
    code: ""
    project: ""
  note: "One concise sentence."
  include_reason: "Why this is an embodied agent work."
```

## Pull Request Checklist

- The work fits the repository scope.
- The entry is placed in the most specific section.
- The README entry uses the compact awesome-list format.
- VLA, world model, simulator, dataset, or low-level-control works are included only when they clearly support embodied-agent memory, reasoning, planning, navigation, manipulation, or evaluation.
- Links are official whenever possible.

## Style

- Keep descriptions short and neutral.
- Prefer official paper, project, code, data, and video links.
- Avoid promotional wording.
- Do not add long summaries to `README.md`; use `papers.yaml` for notes and tags.
- Keep section names broad and stable.
