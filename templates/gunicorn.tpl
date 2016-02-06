workers = 2
bind = '0.0.0.0:{{webport}}'
pidfile= '{{ pid }}'
debug = True
loglevel = 'info'
errorlog = '{{ log }}/gunicorn.log'
daemon = True
