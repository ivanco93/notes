FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# superuser credentials and base url
ENV PROTOCOL=http
ENV BASE_URL_DOMAIN=localhost
ENV PORT=8190
ENV SUPERUSER_USERNAME=admin
ENV SUPERUSER_EMAIL=admin@email.com
ENV SUPERUSER_PASSWORD=admin

EXPOSE 80

RUN python manage.py collectstatic --noinput && ls -l /app/staticfiles

RUN python create_super_user.py

RUN apt-get update && apt-get install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["sh", "-c", "service nginx start && gunicorn --bind 127.0.0.1:8000 main.wsgi:application"]
