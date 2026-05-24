# Query Generation Prompt

> Usato per espandere un topic in 3-5 query di ricerca diverse, per coprire angoli diversi del topic.

---

Generate {{num_queries}} diverse web search queries for the topic below.

**Rules:**
- Each query covers a different angle (history, current state, controversies, applications, ecc.)
- Each query is keyword-rich and specific (not a sentence)
- Each query is 3-8 words
- Output ONLY the queries, one per line, no numbering, no preamble.

Topic: **{{topic}}**

{{#if folder_context}}
Folder context: {{folder_context}}
{{/if}}
