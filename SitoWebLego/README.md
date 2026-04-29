# Progetto Sito Web Lego
## Descrizione del Progetto
Questo progetto riguarda la creazione di un sito web dedicato al mondo dei Lego. Il sito presenterà una vasta gamma di prodotti Lego, insieme alle sue storie interessanti.

### Immagini dei Prodotti
Le immagini dei prodotti verranno presentate in gallerie, rendendo facile per i visitatori esplorare le diverse collezioni disponibile.

### Breve Storia dei Lego
I Lego sono stati inventati nel 1932 in Danimarca e hanno assunto una popolarità mondiale. Oggi rappresentano un hobby per le persone di tutte le età.

### Contenuti Aggiuntivi
Il sito includerà anche articoli e video che mostrano come costruire diversi modelli Lego.

### Struttura del progetto
ProgettoSitoWebLego
| SitoWebLego
├── run.py
|── setup_db.py
|── requirements.txt
|── app
│────── repositories
│──────────── lego_repository.py
│──────────── user_repository.py
│────── templates
│──────────── auth
│────────────────── login.html
│────────────────── register.html
│──────────── about.html
│──────────── aggiungilego.html
│──────────── base.html
│──────────── dashboard.html
│──────────── editlego.html
│──────────── index.html
│────── __init__.py
│────── auth.py
│────── db.py
│────── main.py
│────── schema.sql
|── instance
│────── lego.sqlite

-  link per aprire il Browser --> http://127.0.0.1:5000/