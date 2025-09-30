FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY mail-service.py .
COPY index.html ./static/

# Create necessary directories
RUN mkdir -p /app/mail-storage /app/logs

# Set permissions
RUN chmod +x mail-service.py

# Expose the mail service port
EXPOSE 7005

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:7005/health')"

# Run the mail service
CMD ["python", "mail-service.py"]