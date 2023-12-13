# Semantic Similarity Analysis with spaCy

## Introduction

This repository contains a script (`semantic.py`) that uses spaCy, a natural language processing library, to analyze semantic similarities between words and sentences.

## Instructions

### Prerequisites

- Ensure that you have Python installed on your machine.

### Setup

1. Clone this repository: `git clone https://github.com/mafikaj/semantic-similarity-analysis`
2. Navigate to the project directory: `cd semantic-similarity-analysis`

### Running the Code

3. Install the required dependencies by running: `pip install -r requirements.txt`
4. Run the script: `python semantic.py`

### Observations and Notes

- The script compares word similarities and sentence similarities using spaCy models ('en_core_web_md' and 'en_core_web_sm').
- Make sure to read the comments in the code for detailed insights into the observations.

### Example of My Own

- Consider the words 'car,' 'bicycle,' and 'bus' for higher similarities due to their association with transportation.

### Docker Support (Optional)

- If you prefer running the code in a Docker container, follow these steps:

#### Build Docker Image

5. Build the Docker image: `docker build -t semantic-similarity-analysis.`

#### Run Docker Container

6. Run the Docker container: `docker run semantic-similarity-analysis`

### Additional Notes

- The Dockerfile is configured to use the requirements.txt file for installing dependencies.

Feel free to explore and modify the code for your specific use case!

---

**Note:** The instructions above assume you have Docker installed on your machine. If not, you can skip the Docker-related steps.
