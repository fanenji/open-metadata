---
type: query
title: "Configurazione SSO con Keycloak"
created: 2026-06-26
origin: chat
query: "configurazione sso con keycloak"
tags: [keycloak, sso, oidc, authentication, openmetadata]
---

# Configurazione SSO con Keycloak

La wiki ha **informazioni limitate** sulla configurazione specifica di Keycloak. Ecco cosa è documentato:

## Cosa sappiamo

**Keycloak è supportato** come identity provider OIDC. OpenMetadata espone un client OIDC completo e può integrarsi con Keycloak, Azure AD, Okta e altri provider attraverso il suo framework di autenticazione estensibile [[google-oauth]].

L'integrazione con provider OIDC (es. Keycloak) è il **metodo standard per l'accesso utente** alla UI: OpenMetadata mappa i claim del token OIDC a ruoli interni — `ADMIN`, `DATA_ENGINEER`, `DATA_CONSUMER`, `DATA_STEWARD` [[accesso-openmetadata-senza-login-2026-06-15]].

La configurazione dell'autenticazione avviene nel file `conf/openmetadata.yaml` del backend Java [[google-oauth]] [[openmetadata-code-layout]].

## Distinzione importante: utenti vs bot

L'autenticazione SSO/OIDC (incluso Keycloak) è per **utenti umani** che accedono alla UI. I **bot di ingestion** usano invece un meccanismo separato basato su token JWT pre-generati via certificati SSL, configurato nel blocco `securityConfig` delle pipeline YAML [[bot-authentication]] [[security-config]].

## Cosa NON è documentato

- **Procedura passo-passo** per configurare Keycloak (creazione client OIDC, redirect URI, mappatura claim → ruoli)
- **Parametri specifici** da impostare in `conf/openmetadata.yaml` per Keycloak (client ID, issuer URL, client secret)
- **Claim OIDC attesi** da OpenMetadata e come mapparli lato Keycloak
- **Test/validazione** della configurazione SSO
- Eventuali **limitazioni** o differenze rispetto a Google OAuth (il default)

_(deduzione: poiché Google OAuth è documentato come default con JWT validation su ogni richiesta e Keycloak è citato come alternativa nel framework estensibile, la configurazione seguirà un pattern simile — client OIDC standard con issuer URL, client ID e secret — ma questo non è confermato dalla wiki)_

## Suggerimento

La wiki non contiene una guida operativa per configurare Keycloak. Per ottenerla, si può:
1. Fare `deep-research` sulla documentazione ufficiale OpenMetadata relativa a Keycloak/OIDC
2. Ingerire direttamente la pagina rilevante della doc ufficiale via `wiki-ingest`

## Fonti consultate

- [[google-oauth]]
- [[accesso-openmetadata-senza-login-2026-06-15]]
- [[bot-authentication]]
- [[security-config]]
- [[openmetadata-code-layout]]
- [[oauth-service-principal]]
