#FROM asia.gcr.io/nonprod-utility-233414/base-images/ds-nvidia-base:ds-nvidia-base-cuda11.2-cudnn8-ubuntu20.04-latest

FROM tensorflow/serving
USER root

ENV TZ=US
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY . .


#RUN adduser appuser
#
#USER appuser


#RUN \
#    python3 -m pip install --upgrade pip &&\
#    pip install -r requirements.txt &&\
#    pip install annoy

RUN poetry install --no-dev


#ENV PATH="/home/appuser/.local/bin:$PATH"

EXPOSE 8080

CMD bash scripts/start_server.sh