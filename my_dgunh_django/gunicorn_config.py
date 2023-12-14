command = '/home/dsune-admin/myDGUNH/env/bin/gunicorn'
pythonpath = '/home/dsune-admin/myDGUNH/my_dgunh_django'
bind = '127.0.0.1:8001'
workers = 5
user = 'dsune-admin'
limit_request_field = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=my_dgunh_django.settings'
