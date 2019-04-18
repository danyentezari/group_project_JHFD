web: gunicorn group_project_JHFD.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=group_project_JHFD --loglevel=info
