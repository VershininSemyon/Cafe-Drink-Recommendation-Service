
from multiprocessing import cpu_count


bind = '0.0.0.0:8000'
max_requests = 10_000
worker_class = 'gevent'
workers = cpu_count() * 2 + 1

env = {
    'DJANGO_SETTINGS_MODULE': 'backend.config.settings'
}

reload = True
name = 'Cafe Drink Recommendation Service'
