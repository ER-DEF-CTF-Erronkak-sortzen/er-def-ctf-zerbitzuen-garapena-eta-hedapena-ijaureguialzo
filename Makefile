#!make

services:
	@ansible-playbook -i hosts.ini -u root services-playbook.yml

checkers:
	@ansible-playbook -i hosts.ini -u root checkers-playbook.yml

clean:
	@ansible-playbook -i hosts.ini -u root clean-playbook.yml

status-checker:
	@ssh root@10.255.254.200 'systemctl status ctf-checkermaster@vulnerable'
