#FROM asia.gcr.io/nonprod-utility-233414/base-images/ds-nvidia-base:ds-nvidia-base-cuda11.2-cudnn8-ubuntu20.04-latest

FROM python
USER root

ENV TZ=US
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY . .



#RUN \
#    python3 -m pip install --upgrade pip
#
#RUN \
#    python$PYTHON_VERSION -m pip install -U --no-cache-dir wheel==0.37.1  &&\
#    python$PYTHON_VERSION -m pip install -U --no-cache-dir annoy

#RUN \
#    chown -R appuser:appuser /app && \
#    chmod +x scripts/start_server.sh
RUN adduser appuser

USER appuser

RUN \
   curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/home/appuser/.local/bin":$PATH

RUN poetry install --no-dev --no-interaction

RUN poetry add annoy

EXPOSE 8080

CMD bash scripts/start_server.sh