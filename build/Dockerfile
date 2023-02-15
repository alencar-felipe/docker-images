FROM python:3.12.0a5-bullseye

COPY app /app

WORKDIR app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/app/main.py" ]
