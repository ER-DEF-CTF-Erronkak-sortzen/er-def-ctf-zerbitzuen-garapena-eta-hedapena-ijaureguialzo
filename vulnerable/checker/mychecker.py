#!/usr/bin/env python3

import hashlib
import http.client
import logging
import socket

import paramiko
from ctf_gameserver import checkerlib

PORT_WEB = 80
PORT_PHPMYADMIN = 8080


def ssh_connect():
    def decorator(func):
        def wrapper(*args, **kwargs):
            # SSH connection setup
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            rsa_key = paramiko.RSAKey.from_private_key_file(f'/keys/team{args[0].team}-sshkey')
            client.connect(args[0].ip, username='root', pkey=rsa_key)

            # Call the decorated function with the client parameter
            args[0].client = client
            result = func(*args, **kwargs)

            # SSH connection cleanup
            client.close()
            return result

        return wrapper

    return decorator


class MyChecker(checkerlib.BaseChecker):

    def __init__(self, ip, team):
        checkerlib.BaseChecker.__init__(self, ip, team)
        self._baseurl = f'http://[{self.ip}]:{PORT_WEB}'
        logging.info(f"URL: {self._baseurl}")

    @ssh_connect()
    def place_flag(self, tick):
        flag = checkerlib.get_flag(tick)
        creds = self._add_new_flag(self.client, flag)
        if not creds:
            return checkerlib.CheckResult.FAULTY
        logging.info('created')
        checkerlib.store_state(str(tick), creds)
        checkerlib.set_flagid(str(tick))
        return checkerlib.CheckResult.OK

    def check_service(self):
        # comprobar si los puertos están abiertos
        if not self._check_port_web(self.ip, PORT_WEB):
            logging.error(f"Error de conexión al contenedor: web")
            return checkerlib.CheckResult.DOWN

        if not self._check_port_web(self.ip, PORT_PHPMYADMIN):
            logging.error(f"Error de conexión al contenedor: phpmyadmin")
            return checkerlib.CheckResult.DOWN

        # # check if server is Apache 2.4.50
        # if not self._check_apache_version():
        #     return checkerlib.CheckResult.FAULTY
        #
        # # check if dev1 user exists in pasapasa_ssh docker
        # if not self._check_ssh_user('dev1'):
        #     return checkerlib.CheckResult.FAULTY

        # check if index.hmtl from pasapasa_web has been changed by comparing its hash with the hash of the original file
        if not self._check_file_integrity('vulnerable-web-1',
                                          '/usr/local/apache2/htdocs/index.php',
                                          '5b81e2bd3ef4f7380b65214206a6fa70'):
            logging.error(f"Error de verificación de archivo: index.php")
            return checkerlib.CheckResult.FAULTY

        # # check if /etc/sshd_config from pasapasa_ssh has been changed by comparing its hash with the hash of the original file
        # file_path_ssh = '/etc/ssh/sshd_config'
        # if not self._check_ssh_integrity(file_path_ssh):
        #     return checkerlib.CheckResult.FAULTY

        return checkerlib.CheckResult.OK

    def check_flag(self, tick):
        if not self.check_service():
            return checkerlib.CheckResult.DOWN
        flag = checkerlib.get_flag(tick)
        # creds = checkerlib.load_state("flag_" + str(tick))
        # if not creds:
        #     logging.error(f"Cannot find creds for tick {tick}")
        #     return checkerlib.CheckResult.FLAG_NOT_FOUND
        flag_present = self._check_flag_present(flag)
        if not flag_present:
            return checkerlib.CheckResult.FLAG_NOT_FOUND
        return checkerlib.CheckResult.OK

    @ssh_connect()
    # Function to check if an user exists
    def _check_ssh_user(self, username):
        ssh_session = self.client
        command = f"docker exec pasapasa_ssh_1 sh -c 'id {username}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False
        return True

    @ssh_connect()
    def _check_file_integrity(self, container, path, md5sum):
        ssh_session = self.client
        command = f"docker exec {container} sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False
        output = stdout.read().decode().strip()
        return hashlib.md5(output.encode()).hexdigest() == md5sum

    # Private Funcs - Return False if error
    def _add_new_flag(self, ssh_session, flag):
        # Execute the file creation command in the container
        command = f"docker exec pasapasa_ssh_1 sh -c 'echo {flag} >> /tmp/flag.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)

        # Check if the command executed successfully
        if stderr.channel.recv_exit_status() != 0:
            return False

        # Return the result
        return {'flag': flag}

    @ssh_connect()
    def _check_flag_present(self, flag):
        ssh_session = self.client
        command = f"docker exec pasapasa_ssh_1 sh -c 'grep {flag} /tmp/flag.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False

        output = stdout.read().decode().strip()
        return flag == output

    def _check_port_web(self, ip, port):
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5)
            conn.request("GET", "/")
            response = conn.getresponse()
            return response.status == 200
        except (http.client.HTTPException, socket.error) as e:
            print(f"Exception: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def _check_port_ssh(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            return result == 0
        except socket.error as e:
            print(f"Exception: {e}")
            return False
        finally:
            sock.close()

    @ssh_connect()
    def _check_apache_version(self):
        ssh_session = self.client
        command = f"docker exec pasapasa_web_1 sh -c 'httpd -v | grep \"Apache/2.4.50\'"
        stdin, stdout, stderr = ssh_session.exec_command(command)

        if stdout:
            return True
        else:
            return False


if __name__ == '__main__':
    checkerlib.run_check(MyChecker)
