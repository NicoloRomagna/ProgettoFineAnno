# Documento dei Requisiti – Progetto Sito Web LEGO
## 1. Introduzione
### 1.1 Scopo del documento
Questo documento descrive i requisiti del sito web LEGO, definendo funzionalità e obiettivi del sistema. Serve come riferimento per lo sviluppo e la valutazione del progetto.

### 1.2 Contesto
Il sistema è un'applicazione web che permette agli utenti di esplorare il mondo LEGO, acquistare pezzi singoli e apprendere tecniche di costruzione. È sviluppato come progetto didattico utilizzando tecnologie web standard.

### 1.3 Tema d'esempio
Piattaforma web dedicata ai LEGO con funzionalità di e-commerce semplificato, gestione contenuti e area educativa.

## 2. Obiettivi generali
Creare un sito web informativo e interattivo
Permettere agli utenti di acquistare singoli pezzi LEGO
Offrire contenuti educativi (tutorial e storia LEGO)
Gestire un catalogo di set e componenti

## 3. Stakeholder e attori
Attori principali
Utente non registrato: può visualizzare contenuti e catalogo
Utente registrato: può acquistare e gestire preferenze
Amministratore: gestisce set LEGO e contenuti
Sistema: backend che gestisce dati e logica

## 4. Requisiti funzionali
### 4.1 Requisiti principali
Registrazione utente
Login utente
Gestione sessione
Inserimento nuovi set LEGO (admin)
Eliminazione set LEGO (admin)
Visualizzazione catalogo pezzi
Ricerca pezzi specifici
Selezione e acquisto pezzi
Visualizzazione contenuti educativi
Accesso a tutorial multimediali

### 4.2 User stories
Come utente voglio registrarmi per accedere al sito
Come utente voglio effettuare il login
Come utente voglio cercare pezzi LEGO specifici
Come utente voglio acquistare singoli componenti
Come amministratore voglio aggiungere nuovi set
Come amministratore voglio eliminare set esistenti
Come utente voglio guardare tutorial per costruire modelli
Come utente voglio conoscere la storia LEGO

## 5. Requisiti non funzionali
Prestazioni: caricamento pagine veloce
Usabilità: interfaccia semplice e intuitiva
Sicurezza: gestione sicura delle credenziali
Affidabilità: sistema stabile senza crash
Compatibilità: accessibile da browser moderni
Manutenibilità: codice organizzato e modulare

## 6. Casi d'uso
### 6.1 Casi d'uso essenziali
Registrazione
Login
Ricerca pezzi
Acquisto pezzi
Gestione set (admin)
Visualizzazione tutorial

### 6.2 Descrizione semplificata dei casi d'uso

Esempio: Acquisto pezzi LEGO
L’utente accede al sito
Cerca un pezzo
Seleziona il pezzo desiderato
Lo aggiunge al carrello
Conferma l’acquisto

### 6.3 Relazioni tra casi d'uso: include ed extend
Login include autenticazione utente
Acquisto include selezione prodotto
Tutorial extend esperienza utente
Gestione set include inserimento e cancellazione

### 6.4 Diagramma dei casi d'uso
Da realizzare con PUML:
Attori (utente, admin) collegati a:
Login
Registrazione
Acquisto
Gestione set
Visualizzazione contenuti

## 7. Glossario dei termini
LEGO Set: insieme di pezzi predefiniti
Pezzo: singolo mattoncino LEGO
Minifigure: personaggio LEGO
Catalogo: elenco dei prodotti disponibili
Tutorial: guida alla costruzione
Backend: logica server (Python)
Frontend: interfaccia utente (HTML, CSS)
Database: archivio dati (SQLite)

## 8. Pianificazione e milestone
### 8.1 Gantt semplificato