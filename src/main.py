from fastapi import FastAPI
from src.routers import sys_info,prediction_route
import logging
# from src.logging.configure_logging import configure_logging

app=FastAPI()

app.include_router(sys_info.router)
app.include_router(prediction_route.router)

# @app.on_event("startup")
# def on_startup():
#     # configure logging
#     configure_logging("fast-api worker")
#     logging.info("google cloud logging is configured successfully")