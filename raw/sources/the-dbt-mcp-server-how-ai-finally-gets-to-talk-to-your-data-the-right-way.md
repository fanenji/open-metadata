---
source_url: "https://medium.com/tech-with-abhishek/the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way-9c66654c17d5"
fetched: "2026-04-19"
title: "The dbt MCP Server: How AI Finally Gets to Talk to Your Data (The Right Way)"
author: "Abhishek Kumar Gupta"
published: "2026-04-05"
original_tags: [clippings]
clipped_from: obsidian-web-clipper
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Mastodon](https://me.dm/@abhishekkgupta0)

## [Tech with Abhishek](https://medium.com/tech-with-abhishek?source=post_page---publication_nav-f9b6be363a21-9c66654c17d5---------------------------------------)

[![Tech with Abhishek](https://miro.medium.com/v2/resize:fill:76:76/1*3DNIUqR0e-kHFWIXdq0REQ.png)](https://medium.com/tech-with-abhishek?source=post_page---post_publication_sidebar-f9b6be363a21-9c66654c17d5---------------------------------------)

Real-world AI, Cloud, and Data Engineering articles.

## Why the Model Context Protocol is the most important thing to happen to dbt since incremental models — and how to set it up today

![dbt MCP: The missing link between your AI tools and your trusted data](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jEvqjpTGPcPWU5WNycPb3w.png)

d bt MCP: The missing link between your AI tools and your trusted data

### Something Broke With “AI + Data” — Until Now

Every data team has tried some version of this: connect an LLM to your warehouse, ask it a question about revenue, and watch it confidently return a number that is completely wrong. Not wrong because the AI is bad. Wrong because the AI had no idea what “revenue” means *at your company*. It didn’t know your `fct_orders` model excludes internal test orders. It didn't know your currency conversion logic lives in a macro. It just wrote raw SQL against raw tables and hallucinated a calculation.

This is the foundational problem with AI and enterprise data: **AI systems are powerful reasoners but terrible at knowing what your data actually means.**

> The dbt MCP server is the architectural answer to this problem. It doesn’t just give AI access to data — it gives AI access to governed, documented, semantically understood data. And that changes everything.

## What Is MCP and Why Does It Matter?

Before diving into dbt specifically, let’s understand the protocol itself.

**Model Context Protocol (MCP)** is an open standard — think of it as the USB-C of AI integrations. Before MCP, every AI tool that wanted to connect to an external system had to build a custom, one-off integration. Slack had its own AI plugin format. Notion had its own. GitHub had its own. The result was a fragmented, unmaintainable mess of connectors.

MCP standardizes this. It defines a universal protocol for how AI systems (called **MCP clients** — like Claude, Cursor, VS Code Copilot) connect to external data and tools (called **MCP servers**). Once you build an MCP server, any MCP-compatible AI client can use it without custom code.

> dbt Labs has built an official MCP server for dbt — and it’s genuinely exciting. Here’s why.

## What the dbt MCP Server Actually Does

*The dbt MCP server is a standardized bridge that gives AI applications structured, governed access to everything living inside your dbt project:*

- **Models** — definitions, compiled SQL, column descriptions, schema
- **Metrics** — via the dbt Semantic Layer, with your organization’s actual business logic baked in
- **Lineage** — full upstream and downstream DAG traversal
- **Freshness** — source and model health signals
- **CLI operations** — `dbt run`, `dbt test`, `dbt build`, `dbt compile` — all executable through the AI

Think of it as giving your AI assistant a complete, structured map of your data world — and then also handing it the keys to drive.

The critical insight: **instead of the AI guessing what “monthly recurring revenue” means by reading raw SQL, it can query your pre-defined, version-controlled semantic layer metric and get your company’s actual, governed definition every time.** No hallucination. No drift. No inconsistency.

## Two Flavors: Local vs. Remote MCP Server

The dbt MCP server comes in two forms, each optimized for a different use case.

### Local MCP Server — For Developers

The local MCP server runs on your machine. It’s the full-power option — designed for analytics engineers and data engineers who are actively building dbt projects.

**What it unlocks:**

- Full dbt CLI access (`run`, `test`, `build`, `compile`, `docs`, `show`, `list`, `parse`)
- Code generation (model YAML, source YAML, staging model SQL)
- Column-level lineage via the Fusion engine
- Works with or without a dbt Cloud account
- Works with dbt Core, dbt CLI, and dbt Fusion
- Access to dbt platform APIs when account is connected

**Best for**: Day-to-day development, model authoring, debugging, AI-assisted refactoring

### Remote MCP Server — For Data Consumers

The remote MCP server is hosted by dbt and requires zero local installation. It connects to the dbt platform via HTTP — pure consumption mode.

**What it unlocks:**

- Semantic Layer queries (your governed metrics, live)
- SQL execution against your warehouse
- Metadata discovery (models, sources, lineage, health)
- Administrative API access

**Best for**: Business analysts, stakeholders, non-engineers who want conversational access to data without touching a CLI

> *⚠️* ***Important credit note****:* Only the `text_to_sql` tool consumes dbt Copilot credits. If your Copilot credits run out, the remote MCP server blocks **all tools** — including those proxied from the local server. Monitor your credit usage if you're on a plan with limits.

## The Complete Tool Arsenal

This is where it gets impressive. The dbt MCP server exposes a rich set of tools across seven categories.

### dbt CLI Tools (Local Only)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bJm1agyYHpmNgmdtDs8FcQ.png)

### Semantic Layer Tools (Local + Remote)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bty6WpaN2CijoEb88wVPIg.png)

### Discovery Tools (Local + Remote)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jfZpelZgYmGLdxDBk6D81Q.png)

### SQL Tools (Local + Remote)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sDzPxSuqxllWImP3R3XdIA.png)

### Codegen Tools (Local Only)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*K5wxc9iWQ3x_HSLibykziQ.png)

### Administrative API Tools (Local Only)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vNrJIUF3zDdSwkmbos_HdA.png)

### Fusion Tools (Local + Remote)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xVnCOm_yn44YhvMTHFSW4A.png)

## Three Real-World Use Cases That Actually Matter

### Use Case 1 — Conversational Access to Data (Zero SQL Required)

Imagine a product manager opening Claude Desktop and asking: *“* ***What was our week-over-week growth in user signups for the last quarter, broken down by acquisition channel?****”*

With the dbt MCP server connected, Claude doesn’t write ad-hoc SQL that might calculate “signups” differently from how engineering defined it. It calls `list_metrics`, finds your governed `new_signups` metric in the Semantic Layer, calls `query_metrics` with the right time grain and dimension, and returns a consistent, accurate answer grounded in your organization's actual business logic.

No raw SQL. No hallucinations. No “well, it depends on how you define signup.” Just your metric, your logic, your answer.

### Use Case 2 — Agentic dbt Automation

Indicium, a data consulting company, used the dbt MCP server to build a **migration agent** that automates legacy-to-dbt migrations. The agent can discover existing SQL assets, map them to dbt model patterns, generate staging and intermediate models, validate them with tests, and run them — all autonomously. They reported cutting legacy-to-dbt migration timelines by up to **90%**.

**The workflow looks like this:**

1. Agent calls `get_all_sources` to understand what raw data is available
2. Agent calls `generate_staging_model` to scaffold the initial SQL
3. Agent calls `generate_model_yaml` to create documentation and tests
4. Agent calls `compile` to validate the Jinja/SQL
5. Agent calls `run` to materialize the model
6. Agent calls `test` to validate data integrity
7. Agent calls `get_model_health` to confirm the model is healthy

> **All orchestrated by an LLM. All using your governed dbt context.**

### Use Case 3 — AI-Accelerated Development in Your IDE

Connect the local MCP server to **Cursor** or **VS Code Copilot**, and your IDE becomes dramatically smarter about your dbt project.

**Ask your AI coding assistant:**

- *“Why is this model failing? Here’s the error.”* → It calls `get_job_run_error` to fetch the actual run error, not just what you pasted
- *“What models depend on* `*stg_salesforce__accounts*`*?"* → It calls `get_model_children` for accurate downstream impact
- *“Generate the YAML for this new model.”* → It calls `generate_model_yaml` with column inheritance from upstream
- *“Show me the column-level lineage for* `*order_total*` *in* `*fct_orders*`*."* → It calls `fusion.get_column_lineage` for the full trace

This is what “AI-assisted development” actually looks like when the AI has real project context — not just the file you have open.

## Step-by-Step Setup Guide

Choose your path based on your use case:

### Path A — Local MCP + dbt Platform (Recommended for Engineers)

This gives you full CLI access + platform APIs. Ideal if you’re actively building dbt models.

**Prerequisites**: `uv` installed on your machine (Python package manager)

## Step 1: Install uv

```c
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify: `uv --version`

### Step 2: Find Your dbt Cloud Host URL

1. Log into dbt Cloud
2. Go to **Account Settings → Access URLs**
3. Copy your **Access URL** — it looks like `abc123.us1.dbt.com`

### Step 3: Configure Your MCP Client

**For Claude Desktop:**

1. Open Claude Desktop → **Settings → Developer tab → Edit Config**
2. Paste the following, replacing the placeholder:
```c
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_HOST": "YOUR-ACCESS-URL",
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project",
        "DBT_PATH": "/path/to/your/dbt/executable"
      }
    }
  }
}
```
1. Save and restart Claude Desktop

**For Claude Code (CLI):**

```c
claude mcp add dbt \
  -e DBT_HOST=abc123.us1.dbt.com \
  -e DBT_PROJECT_DIR=/path/to/project \
  -- uvx dbt-mcp
```

**For Cursor:**

1. Go to **Cursor Settings → MCP → Add new global MCP server**
2. Paste this into `mcp.json`:
```c
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_HOST": "YOUR-ACCESS-URL",
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project"
      }
    }
  }
}
```
1. The MCP panel shows the server as connected with tools listed ✅

**For VS Code:**

1. Open **Settings (Cmd/Ctrl+,)** → search for `mcp`
2. Click **Edit in settings.json**
3. Add the same `mcpServers` configuration block under your workspace or user settings
4. Restart VS Code — the GitHub Copilot chat panel now has access to all dbt MCP tools

### Step 4: Authenticate with dbt Platform

The first time you invoke a platform-connected tool (like `list_metrics` or `trigger_job_run`), the server will prompt for OAuth authentication. Follow the browser flow to authorize. Your credentials are stored securely and reused on subsequent calls.

### Step 5: Verify the Connection

In your MCP client, ask:

```c
What dbt models are in my project?
```

The AI should call `get_all_models` and return a list of your actual model names and descriptions. If it does — you're live. ✅

### Path B — Local MCP, No dbt Cloud Account (dbt Core Users)

If you’re on dbt Core without a cloud account, you still get full CLI access.

```c
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project",
        "DBT_PATH": "/path/to/your/dbt/executable"
      }
    }
  }
}
```

> *No* `*DBT_HOST*` *required. You get all CLI tools + local discovery (from* `*manifest.json*`*) — just no Semantic Layer or Admin API.*

### Path C — Remote MCP, Zero Install (Analysts and Consumers)

Perfect for business users or restricted environments. No software installation needed.

1. In your MCP client settings, add the dbt remote MCP endpoint URL (provided by your dbt Cloud account admin via **Account Settings → Integrations → MCP**)
2. Authenticate via OAuth in the browser flow
3. Start querying immediately — `list_metrics`, `query_metrics`, `text_to_sql`, `get_lineage` are all available

You get data access without touching the command line. That’s the point.

## Environment Variables Reference

Fine-tune your local MCP server behavior with these key environment variables:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Z_3eYTUE3pg4InAi_v7mSg.png)

> *💡* ***Security tip****:* Store sensitive variables in a `.env` file and reference it with `--env-file /path/to/.env` in your `uvx` args — never hardcode tokens in your `mcp.json` config file.

## What This Means for the Future of Data Work

Let’s zoom out and appreciate what’s actually happening here.

For years, the promise of “self-service data” was mostly unfulfilled. BI tools made it easier to build charts, but the semantic layer — the *meaning* of data — remained locked inside the heads of data engineers and the SQL of dbt models. Non-technical stakeholders couldn’t access it without help.

MCP changes this equation fundamentally. **The dbt MCP server makes your entire data semantic layer conversational.** Your `fct_orders` model, your `monthly_revenue` metric, your lineage graph, your freshness status — all of it becomes accessible to any AI client, in natural language, with governance preserved end-to-end.

**Three shifts this enables:**

- **From BI dashboards to conversational data**: Analysts stop building charts and start answering questions. The AI queries the governed metric directly — no chart required
- **From manual dbt workflows to agentic pipelines**: Scheduled jobs get augmented by AI agents that can detect anomalies, trigger reruns, debug failures, and report results — autonomously
- **From ad-hoc SQL to governed queries**: `text_to_sql` generates SQL using your project context, not generic patterns — reducing hallucinations dramatically against raw table schemas

The dbt MCP server is not a feature. It’s a **new interface layer** — one that positions dbt not just as a transformation tool, but as the semantic backbone of your entire AI data stack.

## Common Mistakes to Avoid

- **Giving AI full CLI access without understanding the risk**: The CLI tools can modify your warehouse. Only enable `run`, `build`, and `test` in trusted, sandboxed environments. Use `DISABLE_DBT_CLI=true` in production consumption setups
- **Connecting to the wrong environment**: Always verify your `DBT_HOST` points to your intended environment (prod vs. dev). Running `trigger_job_run` against production when you meant staging is a bad day
- **Ignoring Copilot credit consumption**: `text_to_sql` burns credits. In high-usage setups, monitor credit consumption or use `execute_sql` with manually crafted queries instead
- **Skipping the Semantic Layer**: Teams that connect MCP directly to raw table discovery miss the entire point. The power is in querying *governed metrics* — not raw schemas
- **Not pinning the** `dbt-mcp` **version**: `uvx dbt-mcp` always fetches the latest. Pin to a version (`uvx dbt-mcp==0.2.6`) in production setups to avoid breaking changes

## The Bottom Line

The dbt MCP server is the missing link between two worlds that have been awkwardly coexisting: **the governed world of structured data engineering** and **the powerful but ungoverned world of AI**.

Every hour your team spends writing custom AI integrations against raw warehouse tables is an hour building on sand. The dbt MCP server gives you bedrock — your models, your metrics, your lineage, your tests — as the foundation that every AI agent and assistant in your stack can stand on reliably.

**Set it up this week. Your AI tools will be smarter, your stakeholders will be more empowered, and your data will finally mean the same thing everywhere it’s asked about.**

That’s not a small thing. That’s the future of how data teams work.

*👉* ***Enjoyed this?*** *Follow for more deep-dives into dbt, modern data stack, and AI-driven data engineering. Drop your questions or MCP setup experiences in the comments — the community learns together.*

[![Tech with Abhishek](https://miro.medium.com/v2/resize:fill:96:96/1*3DNIUqR0e-kHFWIXdq0REQ.png)](https://medium.com/tech-with-abhishek?source=post_page---post_publication_info--9c66654c17d5---------------------------------------)

[![Tech with Abhishek](https://miro.medium.com/v2/resize:fill:128:128/1*3DNIUqR0e-kHFWIXdq0REQ.png)](https://medium.com/tech-with-abhishek?source=post_page---post_publication_info--9c66654c17d5---------------------------------------)

[Last published Apr 6, 2026](https://medium.com/tech-with-abhishek/dbt-catalog-the-data-discovery-layer-your-team-has-been-missing-edfa91197d89?source=post_page---post_publication_info--9c66654c17d5---------------------------------------)

Real-world AI, Cloud, and Data Engineering articles.

[![Abhishek Kumar Gupta](https://miro.medium.com/v2/resize:fill:96:96/1*EyqcUd4VgjYXp8UQ6vRNiA.jpeg)](https://medium.com/@abhishekkrgupta0?source=post_page---post_author_info--9c66654c17d5---------------------------------------)

[![Abhishek Kumar Gupta](https://miro.medium.com/v2/resize:fill:128:128/1*EyqcUd4VgjYXp8UQ6vRNiA.jpeg)](https://medium.com/@abhishekkrgupta0?source=post_page---post_author_info--9c66654c17d5---------------------------------------)

[86 following](https://medium.com/@abhishekkrgupta0/following?source=post_page---post_author_info--9c66654c17d5---------------------------------------)

I build smart data systems that think, act, and fix themselves. Writing real-world guides on GenAI, LLMs, observability, and everything in between.

## Responses (3)

S Parodi

What are your thoughts?  

```c
Quick question, how do you handle metric aliases? is that included on the list_metrics function?
```

```c
Very good article. Given we are in dbtcore, how would you suggest hosting mcp on a remote host for business users. Is there a community that is working on it? Any advice here would be helpful.
```

```c
Thanks for this good article
Can it be applied to dbt core too?
```