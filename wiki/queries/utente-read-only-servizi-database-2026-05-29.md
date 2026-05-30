---
type: query
title: "Configurare utente read-only su metadati servizi database"
created: 2026-05-29
origin: chat
query: "Configurare su OpenMetadata un utente che ha i diritti di lettura dei metadati di tutti i servizi di tipo database"
tags: [openmetadata, roles, policies, access-control, database]
---

# Configurare utente read-only su metadati servizi database

Per configurare un utente con diritti di sola lettura sui metadati di tutti i servizi database in OpenMetadata, si opera sul framework **Roles & Policies** che implementa il modello ibrido [[hybrid-rbac-abac-model|RBAC-ABAC]].

## Situazione di partenza

OpenMetadata parte già con una baseline collaborativa:

- La **[[default-organization-policy|Default Organization Policy]]** contiene due regole predefinite: `OrganizationPolicy-NoOwner-Rule` e `OrganizationPolicy-Owner-Rule`. Di default, tutti gli utenti autenticati possono visualizzare gli asset.
- Il **[[data-consumer-role|Data Consumer Role]]** è un ruolo preconfigurato per la collaborazione sui dati.

Se non sono state aggiunte policy restrittive (es. Team-Owned Data Protection), un utente standard vede già tutti i metadati.

## Procedura per un ruolo «Database Metadata Reader»

### 1. Creare una Policy con una Rule di sola lettura

**Settings → Policies → Add Policy**, poi aggiungi una Rule:

| Campo          | Valore                                                     |
| -------------- | ---------------------------------------------------------- |
| **Name**       | `DatabaseMetadata-ViewAll-Rule`                            |
| **Effect**     | `Allow`                                                    |
| **Resources**  | `All` (o `DatabaseService`, `Database`, `Schema`, `Table`) |
| **Operations** | `ViewBasic` o `ViewAll`                                    |
| **Condition**  | *(nessuna)*                                                |
|                |                                                            |

### 2. ViewBasic vs ViewAll

- **`ViewBasic`**: descrizione, tag, owner (no profili, sample data, test, query)
- **`ViewAll`**: tutto incluso

Vedi [[viewbasic-viewall-operations]].

### 3. Creare un Ruolo

**Settings → Roles → Add Role**, associa la policy creata.

### 4. Assegnare il Ruolo

Assegnabile direttamente all'utente o al team. Le Policy si assegnano solo ai team, i Ruoli a utenti o team. Vedi [[authorization-policies]].

### 5. Verificare con Permission Debugger

Usa il [[permission-debugger]] per testare gli accessi prima del go-live.

## Avvertenze

- **Deny precede Allow**: regole Deny sovrascrivono sempre Allow. Vedi [[authorization-policies#conflict-resolution-deny-precedence]].
- **Non eliminare la Organization Policy di default**.
- **Scoping ai soli database**: `DatabaseService` è confermato come resource type; per `Database` e `Schema` verificare nella UI. Vedi [[policy-use-cases]].

---

## Service account e autenticazione JWT

### Due meccanismi JWT a confronto

| | **Personal Access Token (PAT)** | **Bot Token (SSL-based)** |
|---|---|---|
| **Generazione** | UI → profilo utente → Access Token tab | Pre-generato con certificati SSL, associato a un Bot |
| **Identità** | Incarna l'utente che l'ha generato | Incarna un bot di sistema (es. `ingestion-bot`) |
| **RBAC/ABAC** | Eredita TUTTI i ruoli e policy dell'utente | Valutato con i ruoli/policy assegnati al bot |
| **Scadenza** | Configurabile: 1h, 1d, 7d, 30d, 60d | Non documentata nella wiki |
| **UI access** | L'utente può anche accedere alla UI | Solo API, niente UI |
| **Caso d'uso tipico** | Script, MCP server, automazione API | Pipeline di ingestion, CLI ingestion |

Fonti: [[personal-access-token]], [[bot-authentication]], [[cli-ingestion-with-basic-auth]]

### Percorso consigliato per script Python: Personal Access Token

#### 1. Crea un utente dedicato

Crea un utente ad-hoc (es. `svc-db-metadata-reader`) e assegna il ruolo `Database Metadata Reader`. Separare i service account dagli utenti umani è buona pratica per audit e governance.

#### 2. Genera un PAT

Da UI: **Profilo → Access Tokens → Generate New Token**. Il token viene mostrato **una volta sola** — copialo e salvalo subito in un secrets manager.

**Attenzione alla scadenza**: i PAT hanno un TTL massimo di **60 giorni** ([[token-expiration]]). Serve una strategia di rotazione prima della scadenza.

#### 3. Usa il PAT negli script

```python
headers = {
    "Authorization": "Bearer eyJraWQiOi...",
    "Content-Type": "application/json"
}
response = requests.get("http://openmetadata:8585/api/v1/tables", headers=headers)
```

#### 4. Il PAT eredita tutti i permessi dell'utente

Il PAT è **identity-preserving** e **permission-aware** ([[personal-access-token#key-properties]]). Ogni chiamata API avrà esattamente i permessi del ruolo assegnato — né più, né meno.

#### 5. Revoca immediata in caso di leak

Da UI: **Profilo → Access Tokens → Revoca**. La revoca è immediata e irreversibile ([[token-revocation]]).

### Raccomandazioni pratiche

1. **Crea un utente dedicato** (`svc-db-metadata-reader`), non riutilizzare un utente umano
2. **Assegna solo il ruolo read-only** — principio del minimo privilegio
3. **Genera il PAT con scadenza 60 giorni** e pianifica la rotazione (remind 7 giorni prima)
4. **Memorizza il token in un secrets manager** (vault, variabile d'ambiente, mai in chiaro nel codice)
5. **Verifica con il [[permission-debugger|Permission Debugger]]** prima di andare in produzione
6. **Prevedi il refresh automatico** negli script: intercetta il 401 e alerta

### Open questions (non documentate nella wiki)

- **Scoping del PAT**: non è documentato se un PAT possa essere limitato a un subset dei permessi dell'utente. L'assunzione è che erediti tutto. _(inferenza)_
- **Numero massimo di PAT per utente**: non noto. Se servono più token, meglio creare più utenti dedicati.
- **Audit log**: non è chiaro se creazione/revoca di PAT vengano registrati negli [[audit-logs]].
- **Struttura interna del JWT**: claims, firma, algoritmo — non documentati.

## Fonti

- `wiki/concepts/roles-and-policies.md`
- `wiki/concepts/authorization-rules.md`
- `wiki/concepts/authorization-policies.md`
- `wiki/concepts/default-organization-policy.md`
- `wiki/concepts/viewbasic-viewall-operations.md`
- `wiki/concepts/spel-conditions.md`
- `wiki/concepts/resource-attributes.md`
- `wiki/concepts/hybrid-rbac-abac-model.md`
- `wiki/synthesis/policy-use-cases.md`
- `wiki/synthesis/user-and-role-management-workflow.md`
- `wiki/entities/data-consumer-role.md`
- `wiki/concepts/bot-authentication.md`
- `wiki/entities/personal-access-token.md`
- `wiki/concepts/token-expiration.md`
- `wiki/concepts/token-revocation.md`
- `wiki/concepts/cli-ingestion-with-basic-auth.md`
- `wiki/queries/managing-users-and-roles-in-openMetadata-2026-05-22-061312.md`
