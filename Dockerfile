# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY config/ ./config/
COPY data/ ./data/
COPY static/ ./static/

# Create logs directory
RUN mkdir -p logs

# Expose port
EXPOSE 8020

# Set environment variables
ENV PYTHONPATH=/app/src
ENV RAG_DIR=/app/data/cache

# Run the application
CMD ["python", "-m", "uvicorn", "src.backends.fastapi_app:app", "--host", "0.0.0.0", "--port", "8020"]
