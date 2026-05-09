---
title: "Designing Data-Intensive Applications with Martin Kleppmann — Summary"
source: "https://www.youtube.com/watch?v=SVOrURyOu_U"
author: "The Pragmatic Engineer (Gergely Orosz)"
guest: "Martin Kleppmann"
published: 2026-04-22
created: 2026-04-24
type: summary
category: library
subcategory: video-transcript
language: en
topics:
  - distributed systems
  - data systems
  - DDIA
  - formal verification
  - local-first software
  - academia vs industry
  - cloud architecture
  - scalability
original_file: "_inbox/clippings/Designing Data-intensive Applications with Martin Kleppmann.md"
---

# Designing Data-Intensive Applications with Martin Kleppmann — Summary

Intervista di Gergely Orosz (The Pragmatic Engineer) a Martin Kleppmann, autore di *Designing Data-Intensive Applications* (DDIA), in occasione dell'uscita della seconda edizione del libro.

---

## 1. Carriera — dalle startup a LinkedIn

### GoTestIt (2008)
Prima startup di Kleppmann: servizio hosted di cross-browser testing per siti web, basato su Selenium. Tecnicamente funzionava ma non riuscì a ottenere adozione perché era difficile convincere i team a integrarlo nel workflow e a investire nella scrittura dei test. Bootstrapped con consulting e piccola quota angel.

### Rapportive (2010–2012)
Seconda startup, molto più riuscita: estensione browser per Gmail che mostrava un profilo social dell'interlocutore (foto, job title da LinkedIn, tweet recenti) accanto all'email. Entrò in Y Combinator in una delle prime batch, si trasferì a San Francisco, raccolse un round. Venduta a LinkedIn nel 2012 con 5 persone in team, in una situazione di pressione: stavano finendo i soldi e non erano riusciti a raccogliere un altro round. **Stack**: Rails + Postgres + Redis — "unexciting", ma con un graph database custom su Postgres per le relazioni.

### LinkedIn — Kafka e stream processing
Dopo l'acquisizione il team rimase insieme e continuò a lavorare su un prodotto derivato (LinkedIn Intro, poi chiuso). Successivamente Kleppmann passò al team di stream processing: Kafka era stato appena open-sourced e lui lavorò su **Samsa**, un framework di stream processing su Kafka.

**Perché LinkedIn costruì Kafka** (da Jay Kreps, "The Log"): il problema era la *data integration* — molti sistemi generavano dati in forma di stream (eventi utente, database) e molti downstream avevano bisogno di consumarli (data warehouse, Hadoop per ML). Kafka nacque come punto di integrazione universale, un'astrazione a bassa soglia ma general-purpose per collegare sorgenti e sink.

Il lavoro a LinkedIn fu rivelatore per Kleppmann: capì come i vari sistemi di dati si connettono, cosa hanno in comune, quali sono i principi fondamentali. Questa comprensione alimentò direttamente la scrittura del libro.

---

## 2. La scrittura di DDIA (prima edizione)

### Motivazione
Il libro nasce dall'esperienza personale: a Rapportive Kleppmann affrontò problemi di performance del database senza avere le fondamenta per diagnosticarli. Voleva scrivere il libro che avrebbe voluto avere allora — una panoramica concettuale ampia, *practitioner-focused*, non un testo teorico né un manuale su un singolo tool, ma un confronto ragionato sui trade-off tra classi di sistemi.

### Processo di apprendimento
Prima di scrivere, Kleppmann imparò parlando con senior engineers di LinkedIn, leggendo research papers e blog post. I numerosi riferimenti alla fine di ogni capitolo sono esattamente le fonti che lui stesso usò per imparare.

### Struttura del libro
La struttura in tre parti (*Foundational Data Systems*, *Distributed Data*, *Derived Data*) è più una classificazione a posteriori. I topic dei capitoli — transazioni, replicazione, partitioning, consistenza, consensus — erano chiari fin dal book proposal. I dettagli interni di ogni capitolo (es. single-leader vs multi-leader vs leaderless per la replicazione) venivano decisi solo quando si scriveva quel capitolo.

### Timeline
~4 anni di scrittura, ~2,5 anni equivalenti full-time. Deadline con O'Reilly mancata di circa 2,5 anni; per la prima edizione l'editore fu accomodante. LinkedIn gli diede il 50% del tempo lavorativo per il libro, ma la coesistenza con il lavoro di engineering e l'on-call era impossibile per il context switching necessario alla scrittura. Alla fine lasciò LinkedIn e si prese una "sabbatical non pagata" (= disoccupazione) per completarlo.

---

## 3. Reliability, Scalability, Maintainability

Le tre qualità nel sottotitolo del libro sono intenzionalmente vaghe, ma Kleppmann le definisce così:

- **Reliability** = fault tolerance: il sistema continua a funzionare anche se un link di rete si interrompe o un nodo crasha. Le tecniche principali: replicazione e ridondanza.
- **Scalability** = meccanismi per gestire aumenti di carico, tipicamente tramite scalabilità orizzontale (shared-nothing, commodity machines). Ma nella seconda edizione emerge anche il **scaling down**: un sistema serverless che costa 13 centesimi/mese con pochissimo traffico è scalabilità nella direzione opposta, altrettanto interessante perché fa sì che il costo sia proporzionale al carico effettivo.
- **Maintainability** = il sistema deve essere comprensibile, modificabile e operabile nel tempo.

---

## 4. Seconda edizione — cosa è cambiato

### Co-autore: Chris Riccomini
Kleppmann era tornato in accademia e aveva perso contatto con le pratiche industry correnti (data lakes, ecc.). Ricordandosi di Chris Riccomini — collega LinkedIn, autore di *The Missing Readme*, autore della newsletter "Materialized View" e investor nel data space — lo contattò per collaborare. La divisione dei ruoli fu efficace: Kleppmann portava lo stile di insegnamento (precisione, accessibilità, parole scelte con cura); Riccomini portava la conoscenza aggiornata dei trend industry.

### Cloud-native architecture — il cambiamento principale
Nella prima edizione l'assunzione implicita era: ogni macchina ha dei dischi locali, il database scrive lì, la replicazione avviene a livello database tra macchine. Oggi questa assunzione è superata. Molti sistemi vengono costruiti su **object store** (S3 e simili) come astrazione fondamentale: la replicazione avviene a livello dello storage layer, non del database. Questo è diverso da EBS (block device su cloud, ma ancora nell'astrazione "disco locale"): un object store è un'astrazione completamente nuova, con comportamenti diversi da un file system. Questo tema è intrecciato attraverso tutto il libro, non isolato in un capitolo.

### Cosa è stato aggiunto
- **Vector indexes** nel capitolo sugli storage engine (indexing strategy per AI/ML)
- **DataFrame** come modello dati (importante per training data, non esclusivo all'AI)
- Coverage più ampia di sistemi cloud-native e managed services

### Cosa è stato rimosso o ridimensionato
- **MapReduce**: "è morto, nessuno lo usa più". Resta nel libro come strumento didattico per capire batch processing shardato, ma la coverage dettagliata della prima edizione è stata tagliata. I successori (Spark, Flink) sono quelli in uso.

---

## 5. Trade-off dell'uso di servizi cloud

**Astrazione vs comprensione degli interni**: Kleppmann rifiuta la preoccupazione che l'uso di managed services renda gli ingegneri "ignoranti". È lo stesso pattern storico dell'industria: garbage collector → non devi più pensare alla memory allocation, e va bene per chi fa business logic. Qualcuno deve comunque implementare quei layer di astrazione — c'è semplicemente specializzazione.

**Quando conoscere gli interni resta utile**: per debuggare comportamenti anomali (es. sapere che un database usa un LSM tree vs B-tree ti dà intuizione sulle performance), per scegliere il servizio giusto, per ragionare sui trade-off costo/disponibilità.

**Multi-region, multi-cloud**: aumenta la disponibilità ma introduce compromessi sulla consistenza. Kleppmann menziona esplicitamente il rischio geopolitico europeo di dipendenza dai cloud US come motivazione per architetture multi-cloud — non più impensabile, anche se ancora improbabile.

---

## 6. Sharding e hardware moderno

Meno urgente rispetto al passato, ma non per via del cloud: principalmente perché l'hardware è molto più potente. Una singola macchina oggi gestisce workload significativi. Replicazione rimane rilevante anche a scale minori, perché serve alla fault tolerance, non alla scalabilità.

---

## 7. I problemi dei sistemi distribuiti

Il capitolo "The Trouble with Distributed Systems" serve a *giustificare* i modelli teorici usati per analizzare i sistemi distribuiti, portando evidenze empiriche (postmortem di tech company, casi reali) che dimostrano perché le assunzioni pessimistiche sono necessarie:

- **Latenza di rete**: non c'è upper bound garantito. Un messaggio può arrivare in 100 µs o non arrivare mai.
- **Crash di nodi**: non è solo software crash — può essere hardware failure, power loss, nodo vivo ma disconnesso dalla rete. Le distinzioni contano per il protocollo di recovery.
- **Clock**: molto tentante assumere che siano corretti; quasi sempre lo sono, ma non possiamo fare affidamento su questa assunzione per algoritmi critici. Nemmeno clock sincronizzati via NTP sono abbastanza precisi.

La moral del capitolo: i failure *capitano*, le edge case strane *capitano*, e chi dice "i failure sono rari, non preoccuparti" ti sta vendendo false certezze. Il trade-off è quanto si investe nella reliability vs il costo di progettazione e operazioni.

---

## 8. Etica per software engineer

Kleppmann inserì questa sezione già nella prima edizione perché in industry vide scarsa attenzione alle implicazioni etiche — startup focalizzate sul prodotto, data harvesting per advertising senza riflessione. Non vuole prescrivere una risposta, ma spingere a *pensarci*.

Punti chiave:
- Gli ingegneri hanno una voce molto forte nel definire i trade-off, anche quelli sociali e reputazionali.
- I rischi da comunicare al business non sono solo tecnici (corruzione dati) ma anche societali (danni da usi inattesi, compliance, reputazione).
- "Vuoi cambiare il mondo? Allora pensare all'impatto delle tue tecnologie è parte del lavoro."
- Nella seconda edizione questa sezione è diventata un capitolo completo.

---

## 9. Formal Verification

### Cos'è
Spectrum di tecniche per provare matematicamente che un sistema soddisfa una specifica:

- **Model checking** (es. TLA+, FSBy): generatore randomizzato di test case che esplora scenari per verificare proprietà. Più accessibile, buon punto di partenza.
- **Proof assistant** (es. Isabelle, Rocq/Coq, Lean): prova formale matematica — non esempi, ma verità su tutti gli stati possibili. Molto più potente ma molto più laborioso.

**Differenza con il testing**: un test verifica alcune istanze di input. Una prova formale ragiona su spazi di stato infiniti — "per ogni possibile i e j, la lunghezza della lista concatenata è i+j".

### Quando vale la pena
Per algoritmi ad alto rischio dove un bug causa corruzione di dati o vulnerabilità di sicurezza. Non economico in industry ordinaria; Kleppmann lo ha usato solo in accademia dove può investire mesi su un singolo algoritmo.

### Perché diventerà più importante con l'AI
Due ragioni:
1. Gli LLM stanno diventando bravi a *scrivere* le prove formali → costo umano si abbassa.
2. Il vibe coding genera grandi quantità di codice che gli umani non possono rivedere manualmente — serve verifica automatizzata. I test tradizionali non bastano; le prove formali possono garantire l'assenza completa di certi tipi di bug, fondamentale in contesti di sicurezza.

### Come iniziare
Kleppmann consiglia di partire dal model checking (TLA+, FSBy), molto più friendly dei proof assistant. Le risorse per imparare i proof assistant sono scarse; lui stesso imparò in pair con colleghi esperti.

---

## 10. Academia vs Industry

### Differenza principale
L'accademia può pensare su scale temporali molto più lunghe, senza la pressione di dover "shippare" in pochi mesi. Permette di lavorare su problemi che vanno contro gli incentivi commerciali (es. local-first software va contro il lock-in che sostiene i business SaaS).

### Cosa può imparare l'industry dall'accademia
Pensiero critico e ragionamento da first principles sui trade-off, invece di "l'ho sentito a una conferenza, ci vado". La fretta in industry porta spesso a short-circuit reasoning.

### Cosa può imparare l'accademia dall'industry
La prospettiva del mondo reale. I PhD student che hanno avuto anni di industry experience sono spesso i più forti, perché hanno breadth of perspective che chi va diretto dall'undergraduate manca.

### Percorso consigliato
Non è una scelta binaria — weave in and out. Anni di industry, poi PhD, o viceversa. L'ibrido produce i risultati migliori.

---

## 11. Local-First Software

Progetto di ricerca principale di Kleppmann (ultimi ~10 anni). L'idea: applicazioni collaborative (tipo Google Docs, Figma) che però non dipendono da un singolo cloud provider — l'utente è in controllo dei propri dati, il fornitore cloud non può "puntarti una pistola alla testa" per il pagamento dell'abbonamento.

**Sfide di engineering** (molto più dure che nella versione centralizzata):

- **Access control in sistemi decentralizzati**: in un sistema centralizzato, il server decide "la revoca arriva prima o l'edit?" In un sistema distribuito/peer-to-peer diversi nodi possono vedere gli eventi in ordine diverso → inconsistenza permanente. Risolvere questo *senza consensus* (per preservare high availability e offline operation) è un problema di ricerca aperto, vicino alla soluzione in **Automerge** (la libreria CRDT di Kleppmann).
- **Timestamp inaffidabili**: in un contesto decentralizzato, un utente con accesso revocato può forgiare timestamp per backdatare un edit e aggirare l'access control → i clock non possono essere usati come arbitri.

Questa area è un esempio di problema che le startup non affrontano perché la soluzione centralizzata è pragmaticamente sufficiente; l'accademia può permettersi di risolvere il problema harder.

---

## 12. Ricerca attuale: Crittografia per le supply chain fisiche

Nuova area di ricerca: usare la crittografia per *provare fatti sul mondo fisico* (es. emissioni di carbonio nella produzione di un prodotto) senza rivelare informazioni commercialmente sensibili (es. l'elenco dei fornitori e le quantità acquistate da ciascuno).

Motivazioni:
- Le normative UE anti-deforestazione (caffè, cacao, olio di palma) richiedono di tracciare esattamente il terreno di origine e verificare che non sia stato deforestato → supply chain provenance.
- Le misurazioni carbon footprint sono spesso inaffidabili o manipolate (greenwashing).

Approccio: zero-knowledge proof o tecniche crittografiche equivalenti che permettano di dimostrare la correttezza della contabilità attraverso le supply chain senza esporre i dati sensibili.

---

## 13. AI nell'educazione informatica

Cambridge mantiene focus sui fondamentali (lambda calculus, algoritmi di base sviluppati negli anni '30), ma l'AI ha cambiato il problema della valutazione. È impossibile e controproducente vietare l'uso dell'AI, ma occorre preservare i *learning outcome* — che sono il vero obiettivo dell'educazione, non gli artefatti (saggi, codice). Cambridge ha introdotto un boot camp per i matricolini su version control, unit testing e generative AI come base comune.

Kleppmann cita lo studio Anthropic/junior engineers: il gruppo che usò AI apprese meno. Il principio generale: a volte bisogna *lottare* con un problema per impararlo. L'AI può essere utile per sbloccarsi su tecnicalismi; è dannosa se sostituisce il grappling con le idee difficili.

---

## 14. Uso personale dell'AI

Kleppmann scrive pochissimo codice in accademia e non ha avuto molto bisogno di AI coding tools. Per la scrittura (libro, papers) preferisce scrivere ogni parola a mano: il processo di scrittura *è* il suo processo di pensiero, e non c'è shortcut. Non è una questione di principio etico, è una questione di processo cognitivo personale. Vede invece valore nell'usare l'AI per ottenere feedback su idee o verificare se un'idea regge all'esame critico.

---

## Punti chiave per un data engineer

1. **Conoscere gli interni dei sistemi che si usano** è ancora un superpotere, anche con managed services: permette di debuggare, scegliere il servizio giusto e fare trade-off consapevoli.
2. **Cloud-native architecture** cambia dove avviene la replicazione (object store layer vs database layer) — il libro aggiornato integra questo perspective ovunque.
3. **Scalabilità verso il basso** (serverless, pay-per-use) è tanto importante quanto la scalabilità verso l'alto.
4. **I failure distribuiti capitano**: clocks, network partitions, crash — i modelli pessimistici sono giustificati da evidenza empirica, non paranoia.
5. **Formal verification + LLM** = combinazione che potrebbe finalmente rendere economicamente praticabile la verifica formale per codice critico.
6. **MapReduce è morto**. Spark e Flink lo hanno sostituito.
7. **Ethics non è optional**: gli ingegneri hanno potere reale di influenzare gli impatti societali dei sistemi che costruiscono.
