

# INTEGRAZIONE


OpenMetadata espone un client OIDC completo che si allinea perfettamente alle capacità di KeyCloak.

Ecco una guida pratica strutturata per passaggi, con i riferimenti alla documentazione ufficiale.

---

### 🔑 1. Configurazione su Keycloak
1. **Crea o seleziona un Realm** (es. `open-metadata`)
2. **Crea un Client**:
   - `Client ID`: es. `open-metadata-ui`
   - `Client authentication`: `ON`
   - `Valid redirect URIs`: `http://<tuo-om-host>:8585/callback` *(o HTTPS se in produzione)*
   - `Valid post logout redirect URIs`: `http://<tuo-om-host>:8585/`
   - `Web origins`: `http://<tuo-om-host>:8585` (o `+` per wildcard se suffice)
3. **Nota i valori da inserire in OpenMetadata**:
   - `Client ID`
   - `Client Secret` (tab `Credentials`)
   - `Issuer URL`: `https://<kc-host>/realms/<realm-name>`
   - `JWKS URL`: solitamente `https://<kc-host>/realms/<realm-name>/protocol/openid-connect/certs`
4. **Configura i Claim**:
   - Vai su `Client scopes` → `describe` → `Client scope details` → `Add predefined protocol mapper`
   - Aggiungi:
     - `groups` (o `roles` a seconda delle tue esigenze)
     - `email`, `preferred_username`, `name` (opzionali ma utili)
   - In `Advanced` del client, assicurati che `Access Token` includa i claim desiderati.

📖 *Doc ufficiale Keycloak*: https://www.keycloak.org/docs/latest/securing_apps/index.html#_oidc_client

---

### ⚙️ 2. Configurazione su OpenMetadata
La configurazione va inserita in `server/application.yaml` (o tramite variabili d'ambiente consigliate per sicurezza).

```yaml
authProviders:
  - type: OIDC
    oidc:
      clientId: "${OIDC_CLIENT_ID}"
      clientSecret: "${OIDC_CLIENT_SECRET}"
      issuer: "${OIDC_ISSUER}"
      redirectUri: "${OIDC_REDIRECT_URI}"
      # Claim per l'autorizzazione (vedere punto 3)
      groupClaimName: "${OIDC_GROUP_CLAIM}"
      adminClaimName: "${OIDC_ADMIN_CLAIM}"
```

**Variabili d'ambiente consigliate** (da passare a `server` e `ingestion` container):
```bash
OIDC_CLIENT_ID=open-metadata-ui
OIDC_CLIENT_SECRET=xxxx-xxxx-xxxx-xxxx
OIDC_ISSUER=https://keycloak.example.com/realms/open-metadata
OIDC_REDIRECT_URI=https://openmetadata.example.com/callback
OIDC_GROUP_CLAIM=groups
OIDC_ADMIN_CLAIM=om-admin # claim uscirà come array nel token
```

📖 *Doc ufficiale OpenMetadata*: https://docs.open-metadata.org/security/authentication#oidc

---

### 🛡️ 3. Autorizzazione (RBAC via Claims)
OpenMetadata mappatura automaticamente i claim nel token OIDC a ruoli interni:
| Claim Key | Ruolo OpenMetadata | Note |
|-----------|-------------------|------|
| `om-admin` o `groups` contenente `admin` | `ADMIN` | Full access + governance |
| `data-engineer` | `DATA_ENGINEER` | Pipeline, schema, lineage |
| `data-consumer` | `DATA_CONSUMER` | Read-only, dashboard, catalog |
| `data-steward` | `DATA_STEWARD` | Classificazione, commenti, policy |

**Esempio di mappatura avanzata** (se i gruppi vengono passati come claim `groups`):
- Utente Keycloak con gruppo `om-admin` → ottiene ruolo `ADMIN` in OpenMetadata
- Utente con gruppo `data-engineer` → `DATA_ENGINEER`
- Utente senza claim specifici → `DATA_CONSUMER` (fallback)

Puoi personalizzare il mapping modificando `groupClaimName` e `adminClaimName` o, nelle versioni più recenti, usando la sezione `roleMapping` (se attiva nella tua release).

---

### ✅ 4. Verifica e Debug
1. **Accesso**: `https://<om-host>/login` → clicca `Login with OIDC` (o Keycloak)
2. **Log**: controlla `server/logs/openmetadata-server.log` per errori di token/issuer
3. **Verifica claim**: usa `jwt.io` (demo mode, non passare secret reali) per vedere come si presenta il token di access/ID di Keycloak
4. **CORS/Redirect**: errori `403` o redirect loop sono quasi sempre dovuti a mismatch tra `redirectUri`, `web origins` e `valid redirect URIs`

---

### 🔗 Risorse Ufficiali
- 🔐 Auth & OIDC: https://docs.open-metadata.org/security/authentication
- 🔑 RBAC & Authorization: https://docs.open-metadata.org/security/authorization
- 🐙 GitHub Issues (costruzione tipici): https://github.com/open-metadata/OpenMetadata/discussions/categories/auth
- 📦 Changelog: https://github.com/open-metadata/OpenMetadata/releases

---

💡 **Vuoi che ti prepari un template completo di `docker-compose.yml` o `values.yaml` (Helm) con le variabili OIDC già iniettate, oppure ti serve aiuto su un errore specifico (es. `invalid_grant`, `redirect_uri_mismatch`, o mappatura ruoli che non si applica)?**