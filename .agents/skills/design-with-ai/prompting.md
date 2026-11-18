---
kind: doc
description: Prompts for creative exploration, prototypes, generated assets and independent critics.
---

# Creative prompting

Used by [design-with-ai](SKILL.md) and linked stage skills when briefing another capability. Write the prompt from current context; do not require the user to repeat it. A prompt is an executable brief, not automatically the endpoint.

Include the relevant domain and audience; goal and output medium/fidelity; fixed decisions and open choices; readable reference images or paths; this iteration's creative question; available authorised tools or skills; and observable success criteria and limits. Distinguish exploratory concepts from specifications and production implementation.

For exploration, request different conceptual or structural interpretations. When using [String Seed of Thought](../ideate-design/exploration.md#string-seed-of-thought), include the interpreted direction and concrete design choices derived from each string, alongside the fixed decisions it must preserve. Follow the linked procedure rather than passing an unexplained string or asking the generator to make random choices. For assets, describe their role, dimensions, integration and required states. For prototypes, state the intended interaction and what fidelity is being tested. Use the [critic procedure](../develop-design/critique.md) for independent review rather than adding builder justifications.

Example generation brief after interpreting a seed: “Explore a monochrome concert archive for collectors. Preserve the supplied wordmark and readable track metadata. String Seed of Thought direction: compact character clusters suggested a catalogue. Express that through dense aligned rows, a narrow index column and small typographic labels. Keep the seed string out of the design. Produce a visual concept, not production code. References establish atmosphere, not layouts to copy.” Other alternatives receive their own seed-derived direction and concrete choices.

A prompt may name multiple available skills and their order. The agent must load and follow them; naming them does not create tools, grant permissions or launch an automatic workflow. Execute the brief only within the user's request, or return it for another environment when that is the requested deliverable.
