FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /install

COPY requirements.txt .

RUN pip install \
    --prefix=/install \
    --no-cache-dir \
    -r requirements.txt

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8000

CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 8000



