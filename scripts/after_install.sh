#!/bin/bash
cd /var/www/html

# 1. Apagar y limpiar cualquier contenedor o red vieja que esté estorbando
# (El '|| true' evita que el script marque error si no encuentra nada que borrar)
sudo /usr/local/bin/docker-compose down || true

# 2. Construir y levantar la versión nueva
sudo /usr/local/bin/docker-compose up -d --build