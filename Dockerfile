FROM python:3.9-slim

#set the working directory for the application
WORKDIR /app

#copy applicattion files to the working directory
COPY requirements.txt .

#install dependencies
RUN pip python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
