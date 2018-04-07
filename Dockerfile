FROM python:2-alpine

RUN ["pip", "install", "markdown", "Jinja2"]

VOLUME /app

CMD ["python", "/app/handout/main.py"]
