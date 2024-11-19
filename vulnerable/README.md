# Vulnerable

Escenario para practicar con SQLi.

## Definición del escenario

| Contendor  | Imagen base | Rol                                                     | Flag                                                     |
|------------|-------------|---------------------------------------------------------|----------------------------------------------------------|
| db         | mariadb     | Base de datos                                           |                                                          |
| web        | php-apache  | Servidor web con una paágina de login vulnerable a SQLi | En el cuerpo de la página `welcome.php` cuando se accede |
| phpmyadmin | phpmyadmin  | Servicio phpMyAdmin (no se utiliza en este escenario)   |                                                          |

## Restricciones

- No se puede detener la web, la base de datos ni el phpMyAdmin.
- No de pueden modificar las páginas `index.php` ni `welcome.php`.
- Si se puede modificar `login.php`.
- Si se puede borrar `info.php`.
- No se puede cambiar la contraseña del usuario de base de datos `vulnerable`.
- Si se puede cambiar la contraseña del `root` de la base de datos.

## Exploit SQLi

### Atacantes

- Analizar el fichero `login.php` y ver que la consulta es susceptible de inyección y que con que la consulta devuelva
  una fila, ya conseguimos el bypass.
- Ejemplo de exploit: `blah') or 1-- `.

### Defensores

- Modificar la consulta para que no sea vulnerable, usando una sentencia preparada.

## Comprobaciones en el checker

- Puerto 80 del servidor web alcanzable.
- Puerto 8080 del servidor de phpMyAdmin alcanzable.
- Healtcheck del contenedor de MariaDB correcto.
- Comprobar la integridad del fichero `ìndex.php`.
- Comprobar la integridad del fichero `welcome.php`.

## Posibles escenarios adicionales

1. Fichero `info.php` olvidado. Eliminar el fichero para eliminar la vulnerabilidad. El flag estaría en un comentario en
   el fuente.
2. Acceso mediante `root` al phpMyAdmin con el password del secret de Compose `Hardc0dedPassw0rd`. Cambiar el password
   para solucionarlo. El flag estará en el campo contraseña del usuario `test@egibide.org`. Este flag también se podría
   conseguir enumerando las filas mediante SQLi.

## Usuarios

- `admin@egibide.org` / `1234`
- `test@egibide.org` / Inválida, podría ser un FLAG en un futuro escenario.
- `root@egibide.org` / `12345`

## Referencias

- [How to set up a simple LAMP server with DOCKER in 3 minutes](https://medium.com/@mikez_dg/how-to-set-up-a-simple-lamp-server-with-docker-images-in-2023-9b0e24476ec6)
- [php - Docker Official Image](https://hub.docker.com/_/php)
- [Initializing a fresh instance](https://hub.docker.com/_/mysql)
- [Use Secrets in Compose](https://docs.docker.com/engine/swarm/secrets/#use-secrets-in-compose)
