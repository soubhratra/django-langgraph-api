# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /app/

# Expose the port
EXPOSE 8000

# Set the working directory to where manage.py is
WORKDIR /app/chatbot_project

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
