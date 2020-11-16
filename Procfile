release: python3 netbox/manage.py collectstatic --no-input
web: gunicorn --pythonpath $PWD --config gunicorn.py --log-file - netbox.wsgi
worker: python3 netbox/manage.py rqworker
