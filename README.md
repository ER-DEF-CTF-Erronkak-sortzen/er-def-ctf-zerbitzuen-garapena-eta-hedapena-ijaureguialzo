[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lgHBPo6Q)

# ctf-gameserver-terraform-services

Set of services to use with original FAUST Attack/Defense CTF gameserver (https://github.com/fausecteam/ctf-gameserver).

Each service has it's README file where you can find more information

## Instalar los servicios

Desde el host garatzaile.

```
ansible-playbook -i hosts.ini -u root services-playbook.yml
```

```
ansible-playbook -i hosts.ini -u root checkers-playbook.yml
```

## Comprobar el estado del checker

```
ssh root@10.255.254.200
systemctl status ctf-checkermaster@vulnerable
```
