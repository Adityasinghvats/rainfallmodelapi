# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt and model file
COPY requirements.txt .
COPY rainfall_prediction_model.pkl .

# Copy the Flask application
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]