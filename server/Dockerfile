# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install Python dependencies
RUN pip install --upgrade pip

# Copy requirements file
COPY requirements.txt .

# Install any additional dependencies
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 5000
 
# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the application using Gunicorn with hot reload enabled
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "--reload", "run:app"]
