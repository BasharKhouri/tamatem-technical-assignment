FROM python:3-slim AS builder

WORKDIR /opt/app

COPY main.py requirements.txt ./
RUN pip install  -r requirements.txt \
	&& useradd -m tamatemUser

USER tamatemUser


CMD ["python3","main.py"]