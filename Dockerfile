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
# CMD ["gunicorn", "filmapp.wsgi:application", "--bind", "0.0.0.0:8000"]


# Base image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (safe minimum)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Render port
EXPOSE 10000

# Start server (Render provides $PORT)
CMD gunicorn filmapp.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads 4 \
    --timeout 120
