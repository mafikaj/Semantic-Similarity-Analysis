# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download spaCy model 'en_core_web_md'
RUN python -m spacy download en_core_web_md

# Run semantic.py when the container launches
CMD ["python", "semantic.py"]