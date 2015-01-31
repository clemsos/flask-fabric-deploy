workers = 2
bind = '0.0.0.0:{{webport}}'
pidfile= '{{ pid }}'
debug = False
loglevel = 'debug'
errorlog = '{{ log }}/gunicorn.log'
daemon = False
