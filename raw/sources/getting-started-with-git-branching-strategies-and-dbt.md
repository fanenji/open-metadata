---
source_url: "https://docs.getdbt.com/blog/git-branching-strategies-with-dbt?version=1.12"
fetched: "2026-04-22"
title: "Getting Started with git Branching Strategies and dbt"
author: "- "Christine Berger"
  - "Carol Ohms"
  - "Taylor Dunlap"
  - "Steve Dowling""
published: "2025-03-10"
clipped_from: obsidian-web-clipper
---
Hi! We’re Christine and Carol, Resident Architects at dbt Labs. Our day-to-day work is all about helping teams reach their technical and business-driven goals. Collaborating with a broad spectrum of customers ranging from scrappy startups to massive enterprises, we’ve gained valuable experience guiding teams to implement architecture which addresses their major pain points.

The information we’re about to share isn't just from our experiences - we frequently collaborate with other experts like Taylor Dunlap and Steve Dowling who have greatly contributed to the amalgamation of this guidance. Their work lies in being the critical bridge for teams between implementation and business outcomes, ultimately leading teams to align on a comprehensive technical vision through identification of problems and solutions.

**Why are we here?**  
We help teams with dbt architecture, which encompasses the tools, processes and configurations used to start developing and deploying with dbt. There’s a lot of decision making that happens behind the scenes to standardize on these pieces - much of which is informed by understanding what we want the development workflow to look like. The focus on having the ***perfect*** workflow often gets teams stuck in heaps of planning and endless conversations, which slows down or even stops momentum on development. If you feel this, we’re hoping our guidance will give you a great sense of comfort in taking steps to unblock development - even when you don’t have everything figured out yet!

There are three major tools that play an important role in dbt development:

- **A repository**  
	Contains the code we want to change or deploy, along with tools for change management processes.
- **A data platform**  
	Contains data for our inputs (loaded from other systems) and databases/schemas for our outputs, as well as permission management for data objects.
- **A dbt project**  
	Helps us manage development and deployment processes of our code to our data platform (and other cool stuff!)

![dbt's relationship to git and the data platform](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/1_dbt_eco.png?v=2)

dbt's relationship to git and the data platform

dbt's relationship to git and the data platform

No matter how you end up **defining** your development workflow, these major steps are always present:

- **Development**: How teams make and test changes to code
- **Quality Assurance**: How teams ensure changes work and produce expected outputs
- **Promotion**: How teams move changes to the next stage
- **Deployment**: How teams surface changes to others

This article will be focusing mainly on the topic of git and your repository, how code corresponds to populating your data platform, and the common dbt configurations we implement to make this happen. We’ll also be pinning ourselves to the steps of the development workflow throughout.

## Why we should focus on git

Source control (and git in particular) is foundational to modern development with or without dbt. It facilitates collaboration between teams of any size and makes it easy to maintain oversight of the code changes in your project. Understanding these controlled processes and what code looks like at each step makes understanding how we need to configure our data platform and dbt much easier.

## ⭐️ How to “just get started” ⭐️

This article will be talking about git topics in depth — this will be helpful if your team is familiar with some of the options and needs help considering the tradeoffs. If you’re getting started for the first time and don’t have strong opinions, **we recommend starting with Direct Promotion**.

Direct Promotion is the foundation of all git branching strategies, works well with basic git knowledge, requires the least amount of provisioning, and can easily evolve into another strategy if or when your team needs it. We understand this recommendation can invoke some thoughts of “what if?”. **We urge you to think about starting with direct promotion like getting a suit tailored**. Your developers can wear it while you’re figuring out the adjustments, and this is a much more informative step forward because it allows us to see how the suit functions *in motion —* our resulting adjustments can be starkly different than what we thought we’d need when it was static.

The best part with ‘just getting started’ is that it’s not hard to change configurations in dbt for your git strategy later on (and we'll cover this), so don’t think of this as a critical decision that will that will result in months of breaking development for re-configuration if you don’t get it right immediately. Truly, changing your git strategy can be done in a matter of minutes in dbt Cloud.

## Branching strategies

Once a repository has its initial commit, it always starts with one default branch which is typically called `main` or `master` — we’ll be calling the default branch `main` in our upcoming examples. The `main` branch is *always the final destination that we’re aiming to land our changes, and most often corresponds to the term "production"* - another term you'll see us use throughout.

***How we want our workflow to look getting our changes from development to `main` is the big discussion***. Our process needs to consider all the steps in our workflow: development, quality assurance, promotion, and deployment. **Branching Strategies** define what this process looks like. We at dbt are not reinventing the wheel - a number of common strategies have already been defined, implemented, iterated on, and tested for at least a decade.

There are two major strategies that encompass all forms of branching strategies: **Direct Promotion** and **Indirect Promotion**. We’ll start by laying these two out simply:

- What is the strategy?
- How does the development workflow of the strategy look to a team?
- Which **repository branching rules and helpers** help us in this strategy?
- How do we commonly configure **dbt Cloud** for this strategy?
- How do branches and dbt processes map to our **data platform** with this strategy?

Then, we’ll end by comparing the strategies and covering some frequently asked questions.

> [!-info] -info
> Know before you go
> 
> There are *many* ways to configure each tool (especially dbt) to accomplish what you need. The upcoming strategy details were written intently to provide what we think are the minimal standards to get teams up and running quickly. These are starter configurations and practices which are easy to tweak and adjust later on. Expanding on these configurations is an exercise left to the reader!

## Direct promotion

**Direct promotion** means we only keep one long-lived branch in our repository — in our case, `main`. Here’s the workflow for this strategy:

![Direct promotion branching strategy](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/2_direct_git.png?v=2)

Direct promotion branching strategy

Direct promotion branching strategy

### How does the development workflow look to a team?

Layout:

- `feature` is the developer’s unique branch where task-related changes happen
- `main` is the branch that contains our “production” version of code

Workflow:

- **Development**: I create a `feature` branch from `main` to make, test, and personally review changes
- **Quality Assurance**: I open a pull request comparing my `feature` against `main`, which is then reviewed by peers (required), stakeholders, or subject matter experts (SMEs). We highly recommend including stakeholders or SMEs for feedback during PR in this strategy because the next step changes `main`.
- **Promotion**: After all required approvals and checks, I merge my changes to `main`
- **Deployment**: Others can see and use my changes in `main` after I merge and `main` is deployed

### Repository branching rules and helpers

At a minimum, we like to set up:

- **Branch protection** on `main` ([like these settings for GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)), requiring:
	- a pull request (no direct commits to `main`)
		- pull requests must have at least 1 reviewer's approval
- **A PR template** ([such as our boiler-plate PR template](https://docs.getdbt.com/blog/analytics-pull-request-template)) for `feature` PRs against `main`

### dbt Cloud processes and environments

Here’s our branching strategy again, but now with the dbt Cloud processes we want to incorporate:

![Direct Promotion strategy with dbt cloud processes denoted](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/3_direct_dbt_deployment.png?v=2)

Direct Promotion strategy with dbt cloud processes denoted

Direct Promotion strategy with dbt cloud processes denoted

In order to create the jobs in our diagram, we need dbt Cloud environments. Here are the common configurations for this setup:

| Environment Name | [Environment Type](https://docs.getdbt.com/docs/dbt-cloud-environments#types-of-environments) | [Deployment Type](https://docs.getdbt.com/docs/deploy/deploy-environments#staging-environment) | Base Branch | Will handle… |
| --- | --- | --- | --- | --- |
| Development | development | \- | `main` | Operations done in the IDE (including creating feature branches) |
| Continuous Integration | deployment | General | `main` | A continuous integration job |
| Production | deployment | Production | `main` | A deployment job |

### Data platform organization

Now we need to focus on where we want to build things in our data platform. For that, we need to set our **database** and **schema** settings on the environments. Here’s our diagram again, but now mapping how we want our objects to populate from our branches to our data platform:

![Direct Promotion strategy with branch relations to data platform objects](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/4_direct_data_population.png?v=2)

Direct Promotion strategy with branch relations to data platform objects

Direct Promotion strategy with branch relations to data platform objects

Taking the table we created previously for our dbt Cloud environment, let's further map environment configurations to our data platform:

| Environment Name | **Database** | **Schema** |
| --- | --- | --- |
| Development | `development` | User-specified in Profile Settings > Credentials |
| Continuous Integration | `development` | Any safe default, like `dev_ci` (it doesn’t even have to exist). The job we intend to set up will override the schema here anyway to denote the unique PR. |
| Production | `production` | `analytics` |

> [!-secondary] -secondary
> note
> 
> We are showing environment configurations here, but a default database will be set at the highest level in a **[connection](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)** (which is a required setting of an environment). *Deployment* environments can override a connection's database setting when needed.

### Direct promotion example

*In this example, Steve uses the term “QA” for defining the environment which builds the changed code from feature branch pull requests. This is equivalent to our ‘Continuous Integration’ environment — this is a great example of defining names which make the most sense for your team!*

<iframe width="640" height="400" src="https://www.loom.com/embed/59c71a9549b5497f99ef86622aad945e" frameborder="0" allowfullscreen=""></iframe>

## Indirect promotion

> [!-info] -info
> A note about Indirect Promotion
> 
> Indirect Promotion introduces more steps of ownership, so this branching strategy works best when you can identify people who have a great understanding of git to handle branch management. Additionally, the ***time from development to production is lengthier*** due to the workload of these new steps, so it requires good project management. We expand more on this later, but it’s an important call out as this is where we see unprepared teams struggle most.

**Indirect promotion** adds other long-lived branches that derive from `main`. The most simple version of indirect promotion is a two-trunk *hierarchical* structure — this is the one we see implemented most commonly in indirect workflows.

*Hierarchical promotion* is promoting changes back the same way we derived the branches. Example:

- a middle branch is derived from `main`
- feature branches derive from the middle branch
- feature branches merge back to the middle branch
- the middle branch merges back to `main`

Some common names for a middle branch as seen in the wild are:

- `qa`: Quality Assurance
- `uat`: User Acceptance Testing
- `staging` or `preprod`: Common software development terminology

We’ll be calling our middle branch `qa` from throughout the rest of this article.

Here’s the workflow for this strategy:

![Indirect Promotion branching strategy](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/6_indirect_git.png?v=2)

Indirect Promotion branching strategy

Indirect Promotion branching strategy

### How does the development workflow look to a developer?

Changes from our direct promotion workflow are highlighted in ==blue==.

Layout:

- `feature` is the developer’s unique branch where task-related changes happen
- ==`qa` contains approved changes from developers’ `feature` branches, which will be merged to main and enter production together once additional testing is complete.`qa` is always ahead of `main` in changes.==
- `main` is the branch that contains our “production” version of code

Workflow:

- **Development**: I create a `feature` branch from ==`qa`== to make, test, and personally review changes
- **Quality Assurance:** I open a pull request comparing my `feature` branch to ==`qa`==, which is then reviewed by peers and ==*optionally*== subject matter experts or stakeholders
- **Promotion**: After all required approvals and checks, I can merge my changes to ==`qa`==
- ==**Quality Assurance**: SMEs or other stakeholders can review my changes in `qa` when I merge my `feature`==
- ==**Promotion:** Once QA specialists give their approval of `qa` ’s version of data, a **release manager** opens a pull request using `qa` ’s branch targeting `main` (we define this as a **“release”**)==
- **Deployment**: Others can see and use my changes (==and other’s changes==) in `main` ==after `qa` is merged to `main`== and `main` is deployed

### Repository branching rules and helpers

At a minimum, we like to set up:

- **Branch protection** on `main` and `qa` ([like these settings for GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)), requiring:
	- a pull request (no direct commits to `main` or `qa`)
		- pull requests must have at least 1 reviewer's approval
- **A PR template** ([such as our boiler-plate PR template](https://docs.getdbt.com/blog/analytics-pull-request-template)) for `feature` PRs against `qa`
- **A PR template** ([such as our boiler-plate PR template for releases](https://github.com/dbt-labs/dbt-proserv/blob/main/.github/release_pull_request_template.md)) for `qa` PRs against `main`

### dbt Cloud processes and environments

Here’s our branching strategy again, but now with the dbt Cloud processes we want to incorporate:

![Indirect Promotion strategy with dbt cloud processes denoted](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/7_indirect_dbt_deployment.png?v=2)

Indirect Promotion strategy with dbt cloud processes denoted

Indirect Promotion strategy with dbt cloud processes denoted

In order to create the jobs in our diagram, we need dbt Cloud environments. Here are the common configurations for this setup:

| Environment Name | [Environment Type](https://docs.getdbt.com/docs/dbt-cloud-environments#types-of-environments) | [Deployment Type](https://docs.getdbt.com/docs/deploy/deploy-environments#staging-environment) | Base Branch | Will handle… |
| --- | --- | --- | --- | --- |
| Development | development | \- | `qa` | Operations done in the IDE (including creating feature branches) |
| Feature CI | deployment | General | `qa` | A continuous integration job |
| Quality Assurance | deployment | Staging | `qa` | A deployment job |
| Release CI | deployment | General | `main` | A continuous integration job |
| Production | deployment | Production | `main` | A deployment job |

### Data platform organization

Now we need to focus on where we want to build things in our data platform. For that, we need to set our **database** and **schema** settings on the environments. There are two common setups for mapping code, but before we get in to those remember this note from direct promotion:

> [!-secondary] -secondary
> note
> 
> We are showing environment configurations here, but a default database will be set at the highest level in a **[connection](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)** (which is a required setting of an environment). *Deployment* environments can override a connection's database setting when needed.

- **Configuration 1**: A 1:1 of `qa` and `main` assets In this pattern, the CI schemas are populated in a database *outside* of Production and QA. This is usually done to keep the databases aligned to what’s been merged on their corresponding branches. Here’s our diagram, now mapping to the data platform with this pattern:
	![Indirect Promotion branches and how they relate to 1\:1 organization in the data platform](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/8_indirect_data_population.png?v=2)
	Indirect Promotion branches and how they relate to 1\\:1 organization in the data platform
	Indirect Promotion branches and how they relate to 1\\:1 organization in the data platform
	Here are our configurations for this pattern:
	| Environment Name | **Database** | **Schema** |
	| --- | --- | --- |
	| Development | `development` | User-specified in Profile Settings > Credentials |
	| Feature CI | `development` | Any safe default, like `dev_ci` (it doesn’t even have to exist). The job we intend to set up will override the schema here anyway to denote the unique PR. |
	| Quality Assurance | `qa` | `analytics` |
	| Release CI | `development` | A safe default |
	| Production | `production` | `analytics` |
- **Configuration 2**: A reflection of the workflow initiative
	In this pattern, the CI schemas populate in a `qa` database because it’s a step in quality assurance. Here’s our diagram, now mapping to the data platform with this pattern:
	![Indirect Promotion branches and how they relate to workflow initiative organization in the data platform](https://docs.getdbt.com/img/blog/2025-01-28-git-branching-strategies-and-dbt/9_alt_indirect_data_population.png?v=2)
	Indirect Promotion branches and how they relate to workflow initiative organization in the data platform
	Indirect Promotion branches and how they relate to workflow initiative organization in the data platform
	Here are our configurations for this pattern:
	| Environment Name | **Database** | **Schema** |
	| --- | --- | --- |
	| Development | `development` | User-specified in Profile Settings > Credentials |
	| Feature CI | `qa` | Any safe default, like `dev_ci` (it doesn’t even have to exist). The job we intend to set up will override the schema here anyway to denote the unique PR. |
	| Quality Assurance | `qa` | `analytics` |
	| Release CI | `qa` | A safe default |
	| Production | `production` | `analytics` |

### Indirect promotion example

*In this example, Steve uses the term “UAT” to define the automatic deployment of the middle branch and “QA” to define what’s built from feature branch pull requests. He also defines a database for each (with four databases total - one for development schemas, one for CI schemas, one for middle branch deployments, and one for production deployments) — we wanted to show you this example as it speaks to how configurable these processes are apart from our standard examples.*

<iframe width="640" height="400" src="https://www.loom.com/embed/0e03faf9f8f7434fbe01eaf7b818e507" frameborder="0" allowfullscreen=""></iframe>

## What did indirect promotion change?

You’ve probably noticed there is one overall theme of adding our additional branch, and that’s supporting our *Quality Assurance* initiative. Let’s break it down:

- **Development**
	While no one will be developing in the `qa` branch itself, it does need a level of oversight just like a `feature` branch needs in order to stay in sync with its base branch. This is because a change now to `main` (like a hotfix or accidental merge) won’t immediately flag our `feature` branches since they are based off of `qa` 's version of code. This branch needs to stay in sync with any change in `main` for this reason.
- **Quality Assurance**
	There are now *two places* where quality can be reviewed (`feature` and `qa`) before changes hit production. `qa` is typically leveraged in at least one of these ways for more quality assurance work:
	- Testing and reviewing how end-to-end changes are performing over time
		- Deploying the full image of the `qa` changes to a centralized location. Some common reasons to deploy `qa` code are:
		- Leveraging [deferral](https://docs.getdbt.com/reference/node-selection/defer) and [Advanced](https://docs.getdbt.com/docs/deploy/advanced-ci) comparison features in CI
				- Testing builds from environment-specific data sets (dynamic sources)
				- Creating staging versions of workbooks in your BI tool. This is most relevant when your BI tool doesn’t do well with changing underlying schemas. For instance, some tools have better controls for grabbing a production workbook for development, switching the underlying schema to a `dbt_cloud_pr_#` schema, and reflecting those changes without breaking things. Other tools will break every column selection you have in your workbook, even if the structure is the same. For this reason, it is sometimes easier to create one “staging” version workbook and always point it to a database built from QA code - the changes then can always be reflected and reviewed from that workbook before the code changes in production.
				- For other folks who want to see or test changes, but aren’t personas that would be included in the review process. For instance, you may have a subject matter expert reviewing and approving alongside developers, who understands the process of looking at `dbt_cloud_pr` schemas. However, if this person now communicates that they have just approved some changes with development to their teammates who will use those changes, the team might ask if there is a way they can also see the changes. Since the CI schema is dropped after merge, they would need to wait see this change in production if there is no process deploying the middle branch.
- **Promotion**
	There are now two places where code needs to be promoted:
	- From `feature` to `qa` by a developer and peer (and optionally SMEs or stakeholders)
		- From `qa` to `main` by a release manager and SMEs or stakeholders
	Additionally, approved changes from feature branches are promoted together from `qa`.
- **Deployment**
	There are now two major branches code can be deployed from:
	- `qa`: The “working” version with changes, `features` merge here
		- `main`: The “production” version
	Due to our changes collecting on the `qa` branch, our deployment process changes from continuous deployment (”streaming” changes to `main` in direct promotion) to continuous delivery (”batched” changes to `main`). Julia Schottenstein does a great job explaining the differences [here](https://www.getdbt.com/blog/adopting-ci-cd-with-dbt-cloud).

## Comparing branching strategies

Since most teams can make **direct promotion** work, we’ll list some key flags for when we start thinking about **indirect promotion** with a team:

- They speak about having a dedicated environment for QA, UAT, staging, or pre-production work.
- They ask how they can test changes end-to-end and over time before things hit production.
- Their developers aren’t the same, or the only, folks who are checking data outputs for validity - especially if the other folks are more familiar performing validations from other tools (like from BI dashboards).
- Their different environments aren’t working with identical data. Like software environments, they may have limited or scrubbed versions of production data depending on the environment.
- They have a schedule in mind for making changes “public”, and want to hold features back from being seen or usable until then.
- They have very high-stakes data consumption.

If you fit any of these, you likely fit into an indirect promotion strategy.

**Strengths and Weaknesses**

We highly recommend that you choose your branching strategy based on which *best supports* *your workflow needs* over any perceived pros and cons — when these are put in the context of your team’s structure and technical skills, you’ll find some aren’t strengths or weaknesses at all!

- **Direct promotion**
	Strengths
	- Much faster in terms of seeing changes - once the PR is merged and deployed, the changes are “in production”.
		- Changes don’t get stuck in a middle branch that’s pending the acceptance of someone else’s validation on data output.
		- Management is mainly distributed - every developer owns their own branch and ensuring it’s in sync with what’s in `main`.
		- There’s no releases to worry about, so no extra processes to manage.
	Weaknesses
	- It can present challenges for testing changes end-to-end or over time in an environment that isn't production. Our desire to build only modified and directly impacted models to reduce the amount of models executed in CI goes against the grain of full end-to-end testing, and our CI mechanism (which executes only upon pull request or new commit) won’t help us test over time.
		- It can be more difficult for differing schedules or technical abilities when it comes to review. It’s essential in this strategy to include stakeholders or subject matter experts on pull requests *before merge,* because the next step is production. Additionally, some tools aren’t great at switching databases and schemas even if the shape of the data is the same. Constant breakage of reports for review can be too much overhead.
		- It can be harder to test configurations or job changes before they hit production, especially if things function a bit differently based on environment.
		- It can be harder to share code that works fully but isn’t a full reflection of a complete task. Changes need to be agreed upon to go to production so others can pull them in, otherwise developers need to know how to pull these in from other branches that aren’t `main` (and be aware of staying in sync or risk merge conflicts).
- **Indirect promotion**
	Strengths
	- There’s a dedicated environment to test end-to-end changes over time.
		- Data outputs can be reviewed either with a developer on PR or once things are in the middle branch.
		- Review from other tools is much easier because we have the option of deploying our middle branch to a centralized location. “Staging” reports can be set up to always refer to this location for reviewing changes, and processes for creating new reports can flow from staging to production.
		- Configurations and job changes can be tested with production-like parameters before they actually hit production.
		- Changes merged to the middle branch for shared development won't be reflected in production. Consumers of `main` will be none-the-wiser about the things that developers do for ease of collaboration.
	Weaknesses
	- Changes can be slower to get to production due to the extra processes intended for the middle branch. In order to keep things moving, there should be someone (or a group of people) in place who fully own managing the changes, validation status, and release cycle.
		- Changes that are valid can get stuck behind other changes that aren’t - having a good plan in place for how the team should handle this scenario is essential because conundrum can hold up getting things to production.
		- There’s extra management of any new trunks, which will need ownership - without someone (or a group of people) who are knowledgeable, it can be confusing understanding what needs to be done and how to do it when things get out of sync.
		- It can require additional compute in the form of scheduled jobs in the QA environment, as well as an additional CI job from `qa` > `main` for testing releases before they're merged.

## Further enhancements

Once you have your basic configurations in place, you can further tweak your project by considering which other features will be helpful for your needs:

- Continuous Integration:
	- [Only running and testing changed models](https://docs.getdbt.com/docs/deploy/ci-jobs#set-up-ci-jobs) and their dependencies
		- Using [dbt clone](https://docs.getdbt.com/reference/commands/clone) to get a copy of large incrementals in CI
- Development and Deployment:
	- Using [schema configurations](https://docs.getdbt.com/docs/build/custom-schemas) in the project to add more separation in a database
		- Using [database configurations](https://docs.getdbt.com/docs/build/custom-databases) in the project to switch databases for model builds

## Frequently asked git questions

**General**

> [!-info] -info
> How do you prevent developers from changing specific files?

> [!-info] -info
> How do you execute other types of checks in the development workflow?

> [!-info] -info
> How do you revert changes?

**Indirect promotion-specific**

> [!-info] -info
> How do you make releases?

> [!-info] -info
> Hierarchical promotion introduces changes that may not be ready for production yet, which holds up releases. How do you manage that?

> [!-info] -info
> What if a bad change made it all the way in to production?

> [!-info] -info
> What if we want to use more than one middle branch in our strategy?

**Direct promotion-specific**

> [!-info] -info
> We need a middle environment and don’t want to change our branching strategy! Is there any way to reflect what’s in development?

> [!-info] -info
> How do we change from a direct promotion strategy to an indirect promotion strategy?