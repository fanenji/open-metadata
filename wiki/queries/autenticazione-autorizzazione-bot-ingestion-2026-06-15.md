---
type: query
title: "Autenticazione e autorizzazione bot ingestion"
created: 2026-06-15
origin: chat
query: "Descrivi la procedura dettagliata per definire autenticazione e autorizzazione per un bot di ingestion"
tags: [authentication, authorization, bots, ingestion, jwt, rbac, abac]
---
# Autenticazione e Autorizzazione per un Bot di Ingestion

Ecco la procedura dettagliata, basata sul meccanismo di [[bot-authentication]].

## 1. Autenticazione: JWT Token del Bot

L'autenticazione dei bot si basa su token JWT pre-generati, diversi dall'autenticazione utente che usa SSO [[bot-authentication]].

**Procedura per ottenere il token:**

1. Accedere alla UI di OpenMetadata
2. Navigare su **Settings** → **Bots**
3. Selezionare l'**`ingestion-bot`** (il bot pre-configurato di sistema)
4. Nella pagina dei dettagli del bot, localizzare il JWT token e cliccare **Copy** [[cli-ingestion-with-basic-auth]]

Il token JWT è generato sulla base dei certificati SSL configurati in OpenMetadata. Quando il bot interagisce con le API del server, presenta questo token: il server lo valida usando i propri certificati SSL, stabilendo così l'identità del bot [[bot-authentication]].

**Personal Access Token (alternativa):** È possibile creare un PAT via UI (Profile → Access Tokens → Generate New Token) con scadenza configurabile (1 ora, 1 giorno, 7 giorni, 30 giorni, 60 giorni). Va incluso nell'header `Authorization: Bearer <token>` [[how-to-create-a-personal-access-token-official-doc-20260514]].

## 2. Configurazione della Pipeline

Nel file YAML di configurazione della pipeline, aggiungere il blocco `securityConfig` sotto `workflowConfig.openMetadataServerConfig` [[security-config]]:

```yaml
workflowConfig:
  openMetadataServerConfig:
    hostPort: http://localhost:8585/api
    authProvider: openmetadata
    securityConfig:
      jwtToken: 'eyJraWQiO...'
```

**Attenzione:** `authProvider` deve essere impostato a `openmetadata` [[security-config]].

Eseguire la pipeline con il CLI:

```bash
metadata ingest -c ./pipeline_name.yaml
```

Il comando `metadata ingest` copre sia estrazione metadati (`type: DatabaseMetadata`) che lineage (`type: DatabaseLineage`) [[metadata-cli]].

## 3. Autorizzazione: Modello Ibrido RBAC-ABAC

Una volta autenticato, il bot è soggetto al modello di autorizzazione [[hybrid-rbac-abac-model]], che valuta **tre fattori** ad ogni richiesta API:

| Fattore | Significato | Dettaglio |
|---|---|---|
| **Who** (Chi) | Identità del bot | Stabilita via JWT token [[bot-authentication]] |
| **What Resource** (Quale Risorsa) | Tabella, Topic, Pipeline, Dashboard, ML Model, Container... | Identificata dalla chiamata API + i suoi [[resource-attributes]] |
| **What Operation** (Quale Operazione) | Create, Delete, ViewAll, ViewTests, ViewQueries... | L'azione richiesta sulla risorsa |

L'autorizzazione è gestita tramite **Roles** (insiemi di permessi) e **Policies** (regole allow/deny), assegnabili a livello di team o utente [[roles-and-policies]].

Per i permessi di visualizzazione, esistono due livelli granulari [[viewbasic-viewall-operations]]:
- **ViewBasic**: solo metadati fondamentali (descrizione, tag, owner)
- **ViewAll**: include anche dati di profiling, sample data, test e query

## 4. Metodi Alternativi di Ingestion

| Metodo | Trigger | Autenticazione |
|---|---|---|
| UI Workflow | Interfaccia OpenMetadata | Sessione utente (OAuth/SSO) |
| CLI con Basic Auth | `metadata ingest` da terminale | JWT token del bot in YAML |
| Kubernetes Native Orchestrator | CronJob / OMJob Operator | JWT token del bot |
| Agent-Based Ingestion | Scheduling UI-driven | Gestito internamente |

Per ambienti automation/CI/CD dove OAuth non è praticabile, la CLI con JWT token è il metodo consigliato [[cli-ingestion-with-basic-auth]].

## 5. Best Practice di Sicurezza

- Usare la **scadenza più breve** possibile per il token (1 ora per CI/CD, fino a 60 giorni per integrazioni stabili) [[token-expiration]]
- **Ruotare i token regolarmente**, rigenerandoli prima della scadenza [[token-expiration]]
- **Conservare il token in modo sicuro**: il token viene mostrato una sola volta dopo la generazione; usare un secrets manager o variabili d'ambiente [[token-expiration]]
- Revocare immediatamente i token compromessi via UI (il meccanismo di revoca interrompe la validità prima della scadenza naturale) [[token-expiration]]

## Gap Rilevati nella Wiki

- La wiki **non documenta** se possano essere usati bot diversi dall'`ingestion-bot` per la CLI ingestion [[cli-ingestion-with-basic-auth]]
- La wiki **non specifica** se i PAT possano essere scoped a permessi o risorse specifiche _(deduzione: dal modello RBAC-ABAC, i permessi dipendono dai ruoli assegnati al bot, non dal token stesso)_
- Le policy di scadenza specifiche per i token bot (vs PAT) **non sono documentate** [[token-expiration]]
- **Non è documentata** l'interazione tra CLI ingestion e Kubernetes native orchestrator: la pipeline esegue localmente o come Job Kubernetes? [[cli-ingestion-with-basic-auth]]

## Fonti consultate

- [[bot-authentication]]
- [[cli-ingestion-with-basic-auth]]
- [[hybrid-rbac-abac-model]]
- [[security-config]]
- [[token-expiration]]
- [[roles-and-policies]]
- [[viewbasic-viewall-operations]]
- [[resource-attributes]]
- [[metadata-cli]]
- `wiki/sources/how-to-create-a-personal-access-token-official-doc-20260514.md`
