# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the dummy_datagen.py script to the working directory
COPY dummy_datagen.py .

# Set the command to run the script
CMD ["python", "dummy_datagen.py"]