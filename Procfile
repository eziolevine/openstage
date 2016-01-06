web: gunicorn config.wsgi:application
worker: celery worker --app=openstage.taskapp --loglevel=info
