import hashlib

print('index.php - ' + hashlib.md5(open('../service/web/htdocs/index.php', 'rb').read()).hexdigest())
print('welcome.php - ' + hashlib.md5(open('../service/web/htdocs/welcome.php', 'rb').read()).hexdigest())
