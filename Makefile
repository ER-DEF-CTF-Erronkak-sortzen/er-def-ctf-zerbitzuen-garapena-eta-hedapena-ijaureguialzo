#!make

help: _header
	${info }
	@echo Opciones:
	@echo -----------------------------------------------------
	@echo services / checkers
	@echo -----------------------------------------------------
	@echo status-checker / status-sub
	@echo -----------------------------------------------------
	@echo ssh-gameserver / ssh-sub-server
	@echo ssh-t1 / ssh-sub-t1 / ssh-t2 / ssh-sub-t2
	@echo -----------------------------------------------------
	@echo exploit / exploit-t1 / exploit-t2
	@echo -----------------------------------------------------
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

status-sub:
	@ssh root@10.255.254.210 'systemctl status ctf-sub*'

exploit:
	@python3 vulnerable/exploit/x1.py

exploit-t1:
	@python3 vulnerable/exploit/x2.py 1 | ssh root@10.0.2.1 'cat > x.flag'

exploit-t2:
	@python3 vulnerable/exploit/x2.py 2 | ssh root@10.0.1.1 'cat > x.flag'

ssh-gameserver:
	@ssh root@10.255.254.200

ssh-t1:
	@ssh root@10.0.1.101

ssh-sub-t1:
	@ssh root@10.0.1.1

ssh-t2:
	@ssh root@10.0.2.101

ssh-sub-t2:
	@ssh root@10.0.2.1

ssh-sub-server:
	@ssh root@10.255.254.210

clean:
	@ansible-playbook -i hosts.ini -u root clean-playbook.yml
