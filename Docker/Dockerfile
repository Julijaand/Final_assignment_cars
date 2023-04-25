FROM python:3.9-slim

#set the working directory for the application
WORKDIR /app
EXPOSE 8000
#copy applicattion files to the working directory
COPY python_app /app

#install dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
