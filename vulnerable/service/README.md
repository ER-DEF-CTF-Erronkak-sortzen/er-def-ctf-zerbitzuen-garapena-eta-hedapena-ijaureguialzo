# sqli-vulnerable-service

Escenario vulnerable.

## Restricciones

- No se puede cambiar la contraseña del usuario de base de datos `vulnerable`.
- No se puede detener la web, la base de datos ni el phpMyAdmin.
- Si se puede cambiar la contraseña del `root`, bloquea un flag accediendo desde el phpMyAdmin.

## Flags

1. Fichero `info.php` olvidado. Eliminar el fichero para eliminar la vulnerabilidad. El flag está en un comentario en el
   fuente.
2. Acceso mediante `root` al phpMyAdmin con el password del secret de Compose `Hardc0dedPassw0rd`. Cambiar el password
   para solucionarlo. El flag estará en la contraseña del usuario `test@egibide.org`.
3. Vulnerabilidad de inyección y bypass de login en los dos campos de formulario. Reescribir la consulta para que no sea
   vulnerable.

## Exploit

```
blah') or 1-- 
```

## Usuarios

- `admin@egibide.org` / `1234`
- `test@egibide.org` / Inválida, es el flag
- `root@egibide.org` / `12345`

## Referencias

- [How to set up a simple LAMP server with DOCKER in 3 minutes](https://medium.com/@mikez_dg/how-to-set-up-a-simple-lamp-server-with-docker-images-in-2023-9b0e24476ec6)
- [php - Docker Official Image](https://hub.docker.com/_/php)
- [Initializing a fresh instance](https://hub.docker.com/_/mysql)
- [Use Secrets in Compose](https://docs.docker.com/engine/swarm/secrets/#use-secrets-in-compose)
