FROM python:3.11

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -rf /tmp

COPY . /app
EXPOSE 8000
CMD ["gunicorn","--bind", "0.0.0.0:8000", "store_app.wsgi:application"]