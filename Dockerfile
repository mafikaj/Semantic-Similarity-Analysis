# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install spaCy and download the model
RUN pip install --no-cache-dir spacy && \
    python -m spacy download en_core_web_md

# Define environment variable
ENV NAME SemanticApp

# Run semantic.py when the container launches
CMD ["python", "./semantic.py"]
