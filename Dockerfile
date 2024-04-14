# Base image with Python 3.9
FROM python:3.9-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the Python requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
