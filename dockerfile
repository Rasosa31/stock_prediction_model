FROM python:3.9-slim

WORKDIR /app

# Copy allthe contents of the repository (include requirements.txt, app.py, data folders)
COPY . /app

#Install dependencies without saving cache
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]