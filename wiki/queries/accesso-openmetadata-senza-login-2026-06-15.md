---
type: query
title: "È possibile accedere a OpenMetadata senza login?"
created: 2026-06-15
origin: chat
query: "è possibile accedere a openmetadata senza fare login?"
tags: [openmetadata, authentication, accesso, login, sicurezza]
---

# È possibile accedere a OpenMetadata senza login?

**No, dalla versione 0.12.1 in poi non è possibile accedere a OpenMetadata senza autenticazione.** L'accesso richiede sempre un login, sia per l'interfaccia utente che per le API/CLI.

## Evoluzione storica

Prima della v0.12.1, OpenMetadata aveva una modalità **no-auth** di default che permetteva l'accesso senza credenziali [[cli-ingestion-with-basic-auth]]. Questa modalità è stata **rimossa** a partire dalla release 0.12.1, che ha introdotto la Basic Auth obbligatoria [[security-config]].

## Come funziona ora

| Canale di accesso | Metodo di autenticazione |
|---|---|
| **UI** | Login via provider SSO/OIDC (Google, Azure AD, Okta, Keycloak, etc.) |
| **CLI / API** | JWT token ottenuto dall'`ingestion-bot` (o altri bot) |

La pagina principale "My Data" è descritta esplicitamente come "The default landing page **after login**" [[understanding-the-basics-of-openmetadata---openmet-20260514]].

L'integrazione con provider OIDC (es. Keycloak) è il metodo standard per l'accesso utente: OpenMetadata espone un client OIDC completo e mappa i claim del token a ruoli interni (ADMIN, DATA_ENGINEER, DATA_CONSUMER, DATA_STEWARD).

## Accesso anonimo/guest

La wiki non documenta alcuna modalità di accesso pubblico, anonimo o guest. Non esistono riferimenti a "public access", "anonymous access" o "guest user".

## Nota storica: visibilità pre-v1.6

Prima della v1.6 esisteva una limitazione per cui utenti non autorizzati potevano vedere l'esistenza degli asset nella tab Explore, pur senza potervi accedere. Questa falla di visibilità è stata risolta con l'introduzione del "search-based RBAC" pianificato per la v1.6.

## Fonti consultate

- [[cli-ingestion-with-basic-auth]]
- [[security-config]]
- [[bot-authentication]]
- `wiki/sources/understanding-the-basics-of-openmetadata---openmet-20260514.md`
- `wiki/sources/how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514.md`
