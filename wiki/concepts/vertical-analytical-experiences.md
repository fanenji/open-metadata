---
type: concept
title: Vertical Analytical Experiences
created: 2026-05-07
updated: 2026-05-07
tags: [analytics, product-category, warehouse-native]
related: [modern-data-stack-history, democratized-data-exploration]
sources: ["The Modern Data Stack Past, Present, and Future.md"]
---
# Vertical Analytical Experiences

Purpose-built analytical interfaces that are native to the modern data stack, identified by Tristan Handy as one of five key opportunity areas for the next wave of data innovation (2021-2025).

## The Problem

The pre-modern-stack era had powerful verticalized analytics tools (Google Analytics, Mixpanel, KissMetrics) but they were data silos — data was locked inside proprietary interfaces and couldn't be joined with other sources. The modern data stack solved the silo problem with horizontal tools that treat all data as rows and columns, but in doing so lost the value of purpose-built analytical experiences.

An analysis tool that sees data as web events can present smarter options than a tool that just sees rows and columns. Google Analytics is more powerful for analyzing web traffic than any generic BI tool.

## The Solution

The article argues for verticalized analytical interfaces built on the modern data stack. Instead of plugging into a proprietary back-end, these tools would plug into the user's data warehouse. The user tells the tool where to find their events table and identifies key fields (user id, timestamp, session id), and the tool compiles all interactions down to SQL.

This was not realistic in 2012, but with fast warehouses, standardized ingestion tools, and open-source modeling, it becomes feasible. The article predicts that companies will be built around single products built in this way, similar to Google Analytics in the prior era.

## Significance

This concept represents a synthesis of the best of both worlds: the power of purpose-built analytical interfaces with the flexibility and integration of the modern data stack. Looker's app marketplace is cited as an early direction, but the opportunity is seen as much larger.