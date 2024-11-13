# Start with the official Python image
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Update pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Expose the port that the Flask app will run on
EXPOSE 8080

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "app:app"]
