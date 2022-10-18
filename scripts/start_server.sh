python scripts/consul_fetch.py
echo 'fetched config folder from consul'

poetry run newrelic-admin run-program \
gunicorn -k uvicorn.workers.UvicornWorker src.main:app --config 'configs/gunicorn_conf.py'

#poetry run ucivorn src.main:app --reload --port 8080