---
type: note
topic:
created: 2026-05-29
tags: []
---
Vedi [[utente-read-only-servizi-database-2026-05-29]]


## Policy

Creata policy:  [DatabaseMetadata-ViewAll](https://openmetadata-test.dataliguria.it/settings/access/policies/DatabaseMetadata-ViewAll) 

Con Rule:
![[Pasted image 20260529094616.png]]

## Role

Creato role: [DatabaseMetadata-ViewAll](https://openmetadata-test.dataliguria.it/settings/access/roles/DatabaseMetadata-ViewAll)
Associato Policy: DatabaseMetadata-ViewAll

## User

Creato user: `meta.sourcer`
Email: meta.sourcer@dataliguria.it
Pwd: 8U+ug3A(
Team: DpTeam
Associato Role: DatabaseMetadata-ViewAll 

## Team

Creato team: service-accounts
Email: service.accounts@dataliguria.it

## Verifica Permessi

Verifica con https://openmetadata-test.dataliguria.it/settings/access/permission-debugger

## Token

Generato PAT

```
eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6Im1ldGEuc291cmNlciIsInJvbGVzIjpbIkRhdGFiYXNlTWV0YWRhdGEtVmlld0FsbCJdLCJlbWFpbCI6Im1ldGEuc291cmNlckBkYXRhbGlndXJpYS5pdCIsImlzQm90IjpmYWxzZSwidG9rZW5UeXBlIjoiUEVSU09OQUxfQUNDRVNTIiwidXNlcm5hbWUiOiJtZXRhLnNvdXJjZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtZXRhLnNvdXJjZXIiLCJpYXQiOjE3ODAwNDkzMjQsImV4cCI6MTc4NzgyNTMyNH0.IUMSYWIOnRGdJH7-83SXThUk2Ol6lPI6BlMpogpfnR3li8k6AUzAHxjjE2DTgKqjQMH9sF7HfM7w5IGW_6N0j37rubzbG_ZUFDzk0w3VlxHpyCW_SO0l7-DLhpBtnbqYo_oo6ZkEOIqR_SdRkfMGtEjabjLLnDBts9Wpr_xS-61S_LDWOPcmbbLpo7FXAZ-BErbDEg1JN4BnDZiuJi6DQUp5s2bhMJcmeh7KYFQluYKEx8QglHSGoDu3c-DNuYUkiKUkNHCifGdZklvI0yo_nqPNMi1zcOLifJkKujuyMv9_v16PF2mxT75I-tUdl39ydMftHQb1LSIfdp7eoBK_aA
```


## PROBLEMA

Associazione al team service-accounts: non riesco a vedere il profilo

![[Pasted image 20260529104435.png|790]]

Se associo al team DpTeam vedo il profilo ma la verifica permessi falliscea causa di alcune policy ereditate da DpTeam
- Quality Bot Policy
- Team only access Policy


SE CANCELLO POLICY -> OK

Perchè associazione a DpTeam e service-accounts sono diverse?
- Su team service-accounts manca policy `Data Consumer Policy` 

