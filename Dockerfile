FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.tt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host","0.0.0.0", "--port","8000"  ]   

# docker pull yourusername/backend:latest

# docker run -p 8000:8000 yourusername/backend