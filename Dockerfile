FROM python:3.12-alpine

WORKDIR /app

# ensure docker does not buffer console output
ENV PYTHONUNBUFFERED=1
# dont write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]