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

---

Pendiente de revisar

---

# Service definition:

- We have two dockers:

1. An Ubuntu (latest version) one which contains the flags.
2. One who has install apache service.
   The attacker has access to a web page (web_docker) and has to look for information that can help him accessing the
   other docker.
   The flags are stored in that last docker's file and attacker has to let them in his T-Submission machine.

# Service implementation:

web docker is configured to take a copy index.html file from the host machine, letting it in '
/usr/local/apache2/htdocs/index.html'.
ssh docker is configured attending to the following tips:

- It has openssh-server installed and started.
- It has a user called 'dev1' whose password is 'w3ar3h4ck3r2'.

'dev1' user's password will never be changed. Moreover, if a team changes it, it will be losing SLa points.

-Flags:
Flags will be stored in 'vulnerable_ssh_1' docker's '/tmp/flags.txt' file.

# About exploting:

- The attacker has to inspect the index.html document; the credentialas are stored there as plain text. With those
  credentials, the attacker can log into vulnerable_ssh docker and take the flags from /tmp/flags.txt.
- The defender should change 'dev1' user's password.

  Attack performed by Team1 against Team 4.
  Inspect web page in 10.0.0.104
  We find 'dev1/w3ar3h4ck3r2' credentials.
  ssh -p 8822 dev1@10.0.0.104
  Enter 'w3ar3h4ck3r2' as password
  cat /tmp/flags.txt
  Copy last flags
  Exit
  'ssh -i /home/urko/Deskargak/keyak/team2-sshkey root@10.0.1.1'
  nano /root/xxx.flag
  Paste copied flags.

  Defense performed by Team4
  'ssh root@10.0.0.104'
  docker exec -it vulnerable_ssh_1 /bin/bash
  passwd dev1

# Checker checks:

- Ports to reach dockers are open (WEB:9797; SSH 8822)
- User 'dev1' exists in vulnerable_ssh docker.
- /etc/sshd_config file from vulnerable_ssh docker has not been changed.
- /usr/local/apache2/htdocs/index.html file's content from vulnerable_web docker has not been changed.

Checks done:

- TEAM 0. Stop the container: 'root@team0-services:~# docker stop vulnerable_web_1' It works OK, service's status
  becomes DOWN.
- TEAM 1. Stop the container: 'root@team0-services:~# docker stop vulnerable_ssh_1' It works OK, service's status
  becomes DOWN.
- TEAM 2. 'userdel dev1'. It works OK, service's status becomes faulty.
- TEAM 3. Change '/etc/sshd_config' file from 'vulnerable_ssh' docker. It works OK, service's status becomes faulty.
- TEAM 4. Change '/usr/local/apache2/htdocs/index.html' file from 'vulnerable_web' docker. It works OK, service's status
  becomes faulty.
- TEAM 5. 'ssh service stop'. It works OK, service's status becomes faulty.
- TEAM 0. apt update apache2

# License notes

Parts from:
https://github.com/kristianvld/SQL-Injection-Playground
