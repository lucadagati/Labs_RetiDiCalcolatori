# Demo FTP con Docker

Questo progetto dimostra come configurare e utilizzare un server FTP (`vsftpd`) e un client FTP (`lftp`) utilizzando Docker.

## Pre-requisiti

- Docker installato sul tuo sistema.

## Build delle Immagini Docker
Vai alla directory del progetto e costruisci le immagini Docker:

```bash
docker build -t ftp-server:latest ./path/to/Dockerfile.server
docker build -t ftp-client:latest ./path/to/Dockerfile.client
```

## Esecuzione del Server FTP
Esegui il container del server FTP:
```bash
docker run -d --name ftp-server -p 20-21:20-21 -p 10090-10100:10090-10100 ftp-server:latest
```

## Esecuzione del Client FTP
Esegui il container del client FTP in modalità interattiva:

```bash
docker run -it --name ftp-client --network host ftp-client:latest
```

## Uso del Client FTP
Una volta avviato il client FTP, connettiti al server:

```bash
lftp ftp://ftpuser:ftppassword@localhost
```

Puoi utilizzare vari comandi FTP come ls, cd, put, get, ecc.

Comandi FTP Comuni
ls: Elenca i file/directory.
cd [directory]: Cambia directory.
put [file]: Carica un file sul server.
get [file]: Scarica un file dal server.
bye: Chiude la connessione.


