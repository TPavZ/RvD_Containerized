FROM python:alpine

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONBUFFERED=1

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN adduser -u 5678 --disabled-password nonroot-user
USER nonroot-user

COPY ./ ./

CMD ["python", "main.py"]