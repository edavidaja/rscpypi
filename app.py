import pypiserver

conf = pypiserver.default_config(password_file="htpasswd.txt", root="./packages")

app = pypiserver.app(**conf)
