# # Base image
# FROM python:3.12-slim

# # Environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt /app/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy project files
# COPY . /app/

# # Expose port
# EXPOSE 8000

# # Run server
# # CMD ["gunicorn", "filmapp.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["gunicorn", "filmapp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2"]





FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (netcat + psycopg requirements)
RUN apt-get update \
    && apt-get install -y netcat-openbsd gcc libpq-dev \
    && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["gunicorn", "filmapp.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT ["./entry.sh"]