FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install fastapi uvicorn python-dotenv jinja2

EXPOSE 8000

CMD ["uvicorn", "src.cat.api.main:app", "--host", "0.0.0.0", "--port", "8000"]