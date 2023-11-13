# Utilizza l'immagine ufficiale di Apache come base
FROM httpd

# Copia il tuo file index.html nella directory del server web Apache nel container
COPY index.html /usr/local/apache2/htdocs/

# Opzionalmente, se vuoi avere curl o wget nel tuo container per scopi dimostrativi:
RUN apt update && apt install -y curl wget
