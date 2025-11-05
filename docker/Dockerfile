<<<<<<< HEAD
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY migration_script.py .

=======
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY migration_script.py .

>>>>>>> 6676fc8 (Initial commit : migration MongoDB + Docker setup)
CMD ["python", "migration_script.py"]