<<<<<<< HEAD
command = '/home/sites/project_root/venv/bin/gunicorn'
pythonpath = '/home/sites/project_root'
bind = '127.0.0.1:8008'
workers = 3
user = 'sites'  # linux user name
=======
command = '/home/sites/toocan_backend/venv/bin/gunicorn'
pythonpath = '/home/sites/toocan_backend'
bind = '0.0.0.0:8008'
workers = 21
user = 'sites'
>>>>>>> 432334e47cc34b2c64ed06bb81847615c877fc46
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=project.settings'
