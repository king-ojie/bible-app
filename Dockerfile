# Stage 1: Build dependencies
FROM python:3.9-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce size
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Stage 2: Runtime image
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY app/ .
EXPOSE 5000
CMD ["python", "main.py"]