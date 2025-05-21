FROM python:3.10

WORKDIR /app

# copy all files and folders from local src to /app in the container
COPY . .

RUN pip install --no-cache-dir -r deps.txt

CMD ["python", "main.py"]