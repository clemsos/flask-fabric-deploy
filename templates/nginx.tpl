server {
        listen          80;
        server_name     {{ domain }};
        root            {{ root }};
 
        access_log      {{ log }}/access.log;
        error_log       {{ log }}/error.log;
 
        location / {
                uwsgi_pass      unix:///{{ socket }};
                include         uwsgi_params;
        }
 
        location /static {
                alias           {{ static }};
        }

}
