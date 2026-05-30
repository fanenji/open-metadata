
Managing users and roles in wiki/sources/OpenMetadata revolves around a dual-layer architecture: a **Role** governs security and permissions, while a **Persona** tailors the user experience. Here is a detailed breakdown of how these components are managed and how they interact.

### 1. Governance Layer: Roles and Policies (The "Hard Boundary")

Roles control what a user is _allowed to do_. They rely on a hybrid RBAC/ABAC model [1].

- **Policies:** These are the fundamental building blocks. A Policy contains specific rules that define the granular logic of access control. Each rule has three key components [1]:
    - **effect:** `Allow` or `Deny`
    - **operations:** Specific actions, e.g., `ViewAll`, `EditDescription`, `Delete`
    - **conditions:** Context-dependent constraints, such as ownership checks or tag-based conditions
- **Roles:** A Role is a container that bundles together multiple Policy IDs [1]. OpenMetadata ships with several pre-defined roles out-of-the-box: `Admin`, `Data Steward`, `Data Engineer`, `Data Analyst`, and `Data Consumer` [1]. Administrators can create custom roles by defining the JSON schema.
- **Assignment:** Roles are assigned to users or teams by administrators to establish their baseline set of permissions [1][29]. Users cannot bypass or change their assigned roles [1].

### 2. Experience Layer: Personas (The "Optimized Environment")

Personas exist to enhance productivity and do **not** confer any permissions [1].

- **Purpose:** Personas control the _presentation layer_ of the UI—landing pages, dashboard widgets, default searches, and suggested tasks [1].
- **Flexibility:** If a user is assigned multiple personas (e.g., Data Engineer and Data Steward), they can **actively switch between them** on the fly to see the most relevant interface for their current task [1].
- **Example:** A user holds the `Data Steward` role (allowing them to edit descriptions and manage tags). However, they prefer to use the `Data Engineer` persona (which displays a landing page focused on pipeline health and technical lineage). Both can be true simultaneously; the Persona simply tailors the interface without compromising the security constraints of the Role [1].

### 3. Managing Users, Teams, and Service Accounts

- **User & Team Hierarchy:** OpenMetadata organizes users into a hierarchical team structure (Organization, Business Unit, Division, Department, Group) [29]. Roles and policies can be applied at any level of this hierarchy.
- **Service Accounts (Bots):** For programmatic or automated access (e.g., via the model-context-protocol for AI agents), OpenMetadata uses dedicated non-human identities. A **Service Account** or **Bot** is created within the platform. Once created, a unique **JSON Web Token (JWT)** is generated for that account, providing a secure, revocable, and scoped method of authentication for automated tools [30].

### 4. Key Limitations to Be Aware Of

- **External Auth Groups:** As of the documented versions, OpenMetadata "does not yet support groups from external authentication providers" [29]. This can affect how users are bulk-managed from an IdP.
- **Pre-v1.6 Asset Visibility:** In versions prior to v1.6, there is a specific limitation where unauthorized users could see the _existence_ of assets (tables, databases, schemas) in the Explore tab UI even if they did not have _access_ to them. Policies restricted access but not visibility. A "search-based RBAC" solution was planned for v1.6 [29].

### Summary of the Management Workflow

1. **Define Policies:** Create rules specifying the `effect`, `operations`, and `conditions`.
2. **Bundle into Roles:** Group these policies into a Role (defined by its JSON schema) [1].
3. **Assign Roles:** Assign the Role to specific Users or Teams within the hierarchical structure [1][29].
4. **Assign Personas (Optional):** Configure Persona settings to curate the UI experience for users based on their job functions [1].
5. **Create Service Accounts (Optional):** For automation, create a Bot and generate a JWT for authentication [30].