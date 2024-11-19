import hashlib

print(hashlib.md5(open('../service/web/htdocs/index.php', 'rb').read().decode().strip().encode()).hexdigest())
print(hashlib.md5(open('../service/web/htdocs/login.php', 'rb').read().decode().strip().encode()).hexdigest())
