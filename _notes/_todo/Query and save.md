---
title: "I Used Karpathy’s LLM Wiki to Build a Research Brain That Updates Itself."
source: "https://pub.towardsai.net/i-used-karpathys-llm-wiki-to-build-a-research-brain-that-updates-itself-ff02dda47335"
author:
  - "[[Adi Insights]]"
  - "[[Innovations]]"
published: 2026-04-19
created: 2026-04-29
description: "I Used Karpathy’s LLM Wiki to Build a Research Brain That Updates Itself. Here’s What Two Weeks Taught Me. Here is a situation every developer who reads a lot will recognise. You have a folder …"
tags:
  - "clippings"
topic:
type: "note"
---
Query is where the compounding pays off. The quality difference from traditional RAG is significant. The LLM is not reading a random chunk from page 14 of a PDF. It is reading a pre-synthesised, cross-referenced encyclopaedia entry that already integrates everything the system has ever learned about that concept from every source ever ingested. When I asked “what does everything I’ve read say about the relationship between context window length and agent reliability,” Claude read the index, identified six relevant wiki pages, and produced a synthesis that referenced four different papers by name and flagged one contradiction between them.

There is one more step that completes the loop: the \` — save\` flag. When enabled, a synthesised answer that represents new, valuable knowledge is automatically filed back as a new wiki page. The slug is derived from the question itself. Future sessions benefit immediately. This is what Karpathy calls the compounding principle. You asked a question, the system answered it, and now the wiki knows the answer too.