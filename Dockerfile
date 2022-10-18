FROM asia.gcr.io/nonprod-utility-233414/base-images/ds-nvidia-base:ds-nvidia-base-cuda11.2-cudnn8-ubuntu20.04-latest

#FROM python
USER root

ENV TZ=US
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY . .

#RUN \
#    python3 -m pip install --upgrade pip &&\
#    python -m pip install poetry \


RUN \
    chown -R appuser:appuser /app && \
    chmod +x scripts/start_server.sh

USER appuser

RUN poetry install --no-dev --no-interaction



EXPOSE 8080

CMD bash scripts/start_server.sh