# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/airbnb_serving/ ./airbnb_serving/

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "airbnb_serving.app:app", "--host", "0.0.0.0", "--port", "8000"]