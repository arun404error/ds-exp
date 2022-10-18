python scripts/consul_fetch.py
echo 'fetched config folder from consul'

#poetry run
newrelic-admin run-program gunicorn --config 'configs/gunicorn_conf.py' src.main:app

#poetry run ucivorn src.main:app --reload --port 8080