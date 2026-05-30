---
type: query
title: "<think>We need to answer the question: \"explain in details h"
created: 2026-05-22
tags: []
---
Managing users and roles in OpenMetadata centers on two tightly integrated concepts: the **hierarchical team structure** for organizing users, and the **Roles & Policies** framework for access control. Administration is performed by users with the Administrator role, which supports a decentralized **multi‑Admin model** where different Admins can independently manage separate teams and departments [12][14].

The sections below walk through the entire process, from setting up the organizational hierarchy to defining advanced authorization rules. All steps are based on the official documentation and wiki synthesis.

---

## 1. Organizing Users with Teams

The foundation of user management is a flexible, multi‑level team hierarchy that mirrors an organisation’s real‑world structure. Teams enable streamlined onboarding, collaboration, and access control [5].

**Team types and hierarchy**  
OpenMetadata provides five team types: **Organization**, **BusinessUnit**, **Division**, **Department**, and **Group**. Only Group teams can directly own data assets. The parent‑child relationships follow strict rules (e.g., a Division can be a child of a BusinessUnit, but not of a Group) [5]. For a  complete matrix, see the [[team-hierarchy-rules]] page.

**Creating teams**  
1. Navigate to **Settings → Team & User Management → Teams**.  
2. Choose the parent team, click **Add Team**, and fill in the required details.  
3. If you want anyone to be able to join the team without an explicit invitation, enable the **Public Team** toggle.  
4. Confirm creation – note that once a team is created as a **Group**, its type cannot be changed later [6].

**Inviting users**  
Go to **Settings → Team & User Management → Users → Add Users**. Provide:  
- **Email** (for sign‑in link)  
- **Display Name**  
- **Description** (optional)  
- **Teams** – the user can be assigned to multiple teams right from the start  
- **Roles** – one or more roles to be assigned directly (the user will also inherit roles from his/her teams)  
- **Admin** – toggle to grant full administrative privileges [7]

**Adding existing users to teams**  
For users already in the platform, navigate to the target team (and sub‑team if needed), go to the **Users** tab, click **Add User**, search for the user, select the checkbox, and click **Update**. Remember that a user inherits all Roles assigned to the teams they belong to [6].

The **multi‑Admin model** allows different Administrators to manage their own team branches, enabling decentralised governance without a single super‑admin bottleneck [14].

---

## 2. Controlling Access with Roles & Policies

Once users are organised into teams, access is governed by **Roles** (named collections of permissions) and **Policies** (rules that define what is allowed or denied). Policies are built from atomic **Rules**, which evaluate the **user identity**, **resource attributes**, and the **requested operation** – a hybrid **RBAC‑ABAC** model [2][4].

### 2.1 Core Building Blocks

| Concept | Description |
|---------|-------------|
| **Rule** | A named condition with an **Effect** (Allow / Deny), a set of **Resources** (e.g., Table, DatabaseService), **Operations** (ViewBasic, ViewAll, EditAll, Delete, etc.), and an optional **SpEL Condition** (e.g., `isOwner()`, `matchAllTags('PII.Sensitive')`). Deny always takes precedence over Allow [2][4]. |
| **Policy** | A collection of Rules. Policies can be assigned to both users and teams. When assigned to a team, the policy is inherited by all members and flows down through the team hierarchy [4]. |
| **Role** | A named bundle of Policies. A Role can be assigned to users or teams. Think of it as a job function profile (e.g., “Data Steward”, “Service Owner”) [4][10]. |
| **ViewBasic vs ViewAll** | Two special operations: **ViewBasic** grants access to basic metadata (description, tags, owner), while **ViewAll** additionally includes profile data, sample data, tests, and queries [2]. |

### 2.2 Default behaviour

Every organization starts with the **Default Organization Policy**, which has two rules:
- **OrganizationPolicy‑NoOwner‑Rule**—allows everyone to view and edit description/tags when no owner is set.  
- **OrganizationPolicy‑Owner‑Rule**—when an owner exists, only the owner or admins can edit.

Do not delete this baseline; layer your custom policies on top of it to enable basic collaboration [17].

### 2.3 Practical design patterns (official use cases)

The documentation provides four concrete scenarios that illustrate how to create effective Roles & Policies [10][17]:

1. **Service Creation Delegation (ServiceOwner role)** – Empower teams to create Database Services, Ingestion Pipelines, and Workflows without Admin help. Create a role with a policy granting **All** operations on `DatabaseService`, `IngestionPipeline`, and `Workflow` [10].

2. **Data Steward Governance (Data Steward role)** – A two‑rule policy:  
   - Allow **All** operations on Glossary and Glossary Term resources.  
   - Allow **EditDescription** and **EditTags** on all entities.  
   This separates governance from platform administration [10].

3. **Team‑Owned Data Protection** – A Deny rule with condition `!isOwner() && !matchTeam()` that prevents anyone outside the owning team from accessing a data asset. This ties access tightly to [[data-asset-ownership]][10].

4. **Tag‑Based Access Control (PII.Sensitive)** – A Deny rule using `matchAllTags('PII.Sensitive') && !isOwner() && !matchTeam()` that restricts access to tables tagged `PII.Sensitive` to the owning user or team. This integrates the [[glossary-tags]] system with authorization, making tags actionable security attributes [10][16].

> **Design principle**: Start with the default Organization Policy, add Allow rules for specific capabilities, and use Deny rules for restrictions. SpEL conditions provide dynamic, attribute‑based decisions [17].

### 2.4 Where to manage it all

All team and user management, as well as Roles & Policies creation, happens under **Settings** (the gear icon), which is accessible to Administrators and users with the appropriate permissions [12]:

- **Teams & Users** → create teams, invite users, assign users to teams.  
- **Roles** → define new Roles and bundle existing Policies.  
- **Policies** → create new Policies by combining Rules.  

For troubleshooting permission issues, use the built‑in **Permission Debugger** (`Settings → Permission Debugger`) that simulates access checks and shows exactly which Rules matched and decided the outcome [4][12].

---

## 3. Putting It All Together – The Recommended Workflow

A typical administration sequence [5][12]:

1. **Establish your organisational hierarchy** – Create teams (BusinessUnit, Division, Department, Group) that mirror your real‑world structure.  
2. **Invite users** – Add them to the appropriate teams, optionally attaching one or more Roles directly.  
3. **Assign baseline access** – Keep the default Organization Policy. Create additional Roles tailored to your departments (e.g., ServiceOwner, DataSteward).  
4. **Layer restrictive policies** – Add Deny rules for sensitive data (tag‑based) or to confine teams to their own assets.  
5. **Verify with the Permission Debugger** – Confirm that the intended effective permissions are in place before going live.  

This layered approach – Teams for grouping, Roles & Policies for permission – gives you fine‑grained, scalable user and access management across the entire data estate.

<!-- cited: 2, 4, 5, 6, 7, 10, 12, 14, 16, 17 -->