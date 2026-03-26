# base image
FROM python:3.12-slim

#working directory
WORKDIR /app

#copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy project files
COPY . .

#port
EXPOSE 8000

# command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
