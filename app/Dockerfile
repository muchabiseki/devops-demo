# --- Builder stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install all dependencies including pytest
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# --- Final stage ---
FROM python:3.11-slim

WORKDIR /app

# Copy installed site-packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy app code
COPY --from=builder /app /app

# Ensure pytest is available in final image
RUN pip install --upgrade pip && pip install pytest

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]