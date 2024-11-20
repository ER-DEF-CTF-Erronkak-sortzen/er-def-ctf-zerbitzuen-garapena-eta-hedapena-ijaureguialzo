#!make

help: _header
	${info }
	@echo Opciones:
	@echo -----------------------------------------------------
	@echo services / checkers
	@echo status-checker
	@echo exploit
	@echo ssh-gameserver / ssh-t1 / ssh-t2 / ssh-sub-t1
	@echo clean
	@echo -----------------------------------------------------

_header:
	@echo -----------------------
	@echo CTF Gameserver Services
	@echo -----------------------

services:
	@ansible-playbook -i hosts.ini -u root services-playbook.yml

checkers:
	@ansible-playbook -i hosts.ini -u root checkers-playbook.yml

status-checker:
	@ssh root@10.255.254.200 'systemctl status ctf-checkermaster@vulnerable'

exploit:
	@python3 vulnerable/exploit/x1.py

ssh-gameserver:
	@ssh root@10.255.254.200

ssh-t1:
	@ssh root@10.0.1.101

ssh-t2:
	@ssh root@10.0.2.101

ssh-sub-t1:
	@ssh root@10.255.254.210

clean:
	@ansible-playbook -i hosts.ini -u root clean-playbook.yml
