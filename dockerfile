# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]