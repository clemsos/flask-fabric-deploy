[uwsgi]

uid = www-data
gid = root
chmod-socket = 666
chown-socket=www-data:www-data

master = true
processes = 2

virtualenv = {{ venv }}
pythonpath = {{ app }}
pidfile = {{ pid }}
socket = {{ socket }}

module = wsgi
callable = app
logdate = true

master = true

; forward requests to the socket.io server
route = /socket.io http:127.0.0.1:8080

; start and monitor the socket.io server
attach-daemon = node myserver.js

; offload proxying, so django processes are not blocked
offload-threads = 2
