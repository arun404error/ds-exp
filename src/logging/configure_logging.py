import json
import logging
from logging.config import dictConfig

from google.cloud.logging import Client

from configs.env_configs import cloud_logger_config


def configure_logging(name):
    print(f"configuring logging for {name}")
    try:
        with open("resources/log_config.json") as f:
            log_config = json.load(f)
            log_config["handlers"]["google_cloud"] = {
                "class": "google.cloud.logging.handlers.CloudLoggingHandler",
                "client": Client.from_service_account_json(cloud_logger_config["credentials_path"]),
                "labels": cloud_logger_config.get("labels", {
                    "app": "not-configured",
                    "environment": "not-configured"
                })
            }
            for logger in log_config["loggers"].keys():
                logging.getLogger(logger).setLevel(cloud_logger_config["level"])
            dictConfig(log_config)
    except KeyError as e:
        logging.error(e)
        raise Exception("Cloud Logging credentials file is not found in configuration or doesn't exist.")
    except FileNotFoundError as e:
        logging.error(e)
        raise Exception("log config did not found at resources/log_config.json")
    except json.JSONDecodeError as e:
        logging.error(e)
        raise Exception("log config is not in proper json format")
