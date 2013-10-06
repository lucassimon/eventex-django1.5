bind = "127.0.0.1:9000"
workers = 5
pidfile = "/home/eventex/run/eventex-site.pid"
accesslog = "/home/eventex/logs/gunicorn/gunicorn-access-eventex-site.log"
errorlog = "/home/eventex/logs/gunicorn/gunicorn-error-eventex-site.log"
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'http',
                         'X-FORWARDED-PROTO': 'http',
                         'X-FORWARDED-SSL': 'off'}
