---
created: 2026-04-30
tags:
  - note
  - journal
---
https://gitlab-test.dataliguria.it/data-platform/infrastracture/applications/jupyter

---


**Sicurezza**

- `allow_all: true` è permissivo — valuta una whitelist esplicita tramite `allowed_users` o gruppi Keycloak (`allowed_groups`) se non tutti gli utenti del realm devono accedere
- `create_system_users: true` crea utenti Unix nel pod hub — verifica che sia intenzionale e non un residuo di configurazione
- Il `secretToken` del proxy dovrebbe essere lungo almeno 32 byte casuali; assicurati che la variabile d'ambiente sia gestita con un Secret k8s e non hardcodata nel pipeline

---

**Risorse**

- **1 CPU guarantee per utente è basso** per un ambiente dbt — se gli utenti eseguono `dbt run` con molti modelli, possono saturarla. Valuta almeno 2 CPU con limit più alto (es. `guarantee: 1, limit: 4`) per permettere bursting
- **20Gi di storage** può essere insufficiente se gli utenti scaricano dataset localmente; dipende dall'uso previsto
- Considera `singleuser.extraResource` per GPU se in futuro servono workload ML

---

**Stabilità / Timeout**

- I timeout websocket (3600s) sono coerenti tra proxy, nginx e Tornado — ma non c'è un `culling` configurato. Senza `cull_idle_timeout`, i server degli utenti non vengono mai spenti automaticamente: spreco di risorse. Aggiungi:

yaml

```yaml
hub:
  config:
    JupyterHub:
      shutdown_on_logout: false
  extraConfig:
    cull-config: |
      c.JupyterHub.services = [{
        'name': 'cull-idle',
        'admin': True,
        'command': ['python3', '-m', 'jupyterhub_idle_culler',
                    '--timeout=3600', '--max-age=28800']
      }]
```

---

**Scheduling**

- Con `userScheduler: false` e risorse `Guaranteed`, i pod vanno su nodi casuali — va bene, ma se il cluster è piccolo valuta di abilitarlo per evitare frammentazione
- Manca `singleuser.profileList`: se in futuro servono profili diversi (es. "small" / "large"), è più facile aggiungerlo subito nella struttura

---

**Ingress**

- L'ingress commentato (produzione) ha `cert-manager` mentre quello attivo usa `wildcard-tls` statico — assicurati che il wildcard venga rinnovato prima della scadenza, altrimenti la sessione cade senza preavviso
- Manca `nginx.ingress.kubernetes.io/proxy-body-size` — il default nginx è 1MB; se gli utenti caricano file via UI potrebbero avere errori 413

---

**Osservabilità**

- Nessuna configurazione di logging strutturato o integrazione con un sistema di monitoring — valuta almeno `hub.extraEnv` per esportare metriche verso Prometheus se il cluster ce l'ha

---

**Priorità suggerita** per un ambiente di test che potrebbe diventare produzione:

1. Idle culler (impatto immediato sui costi)
2. `proxy-body-size` (bug latente)
3. Restrizione accesso OAuth
4. Revisione risorse CPU