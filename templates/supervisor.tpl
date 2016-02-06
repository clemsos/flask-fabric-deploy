[program:{{ domain }}]

directory={{ app_dir }}
environment=PYTHONPATH={{ venv_path}}/bin

command={{venv_path}}/bin/gunicorn wsgi:{{ application }} -c {{gunicorn_conf}}

;user=www-data
autostart=true
autorestart=true

redirect_stderr=true
stopsignal=QUIT
exitcodes=0
