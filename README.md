
## Description
This Python application converts images into a single PDF document.

## Requirements
- Python 3.9
- Docker
- pip packages from `requirements.txt`

## Installation

### 1. Clone the repository
Clone the GitHub repository to your local machine:


### 2. Build the Docker image
After cloning the repository, build the Docker image using the following command:


This will create a Docker image tagged as `convertor-app`.

## Run Command

To run the Docker container with the images and output folders mounted, execute the following command:


This will process all images in the `images` folder and output a PDF in the `output` folder.
