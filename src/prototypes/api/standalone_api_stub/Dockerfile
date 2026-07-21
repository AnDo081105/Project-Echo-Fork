FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/prototypes/api/standalone_api_stub/app ./app
ENV MAX_CONCURRENCY=2
EXPOSE 8000

# Keep this prototype single-process so local debugging stays simple.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
