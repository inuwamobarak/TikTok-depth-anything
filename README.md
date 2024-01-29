# TikTok-depth-anything

This project demonstrates the integration of TikTok's "Depth Anything" monocular depth estimation model into a web application using Flask. The web app allows users to generate depth estimation for images, with a download option for the generated depth image.

![image_90unhlp-thumbnail_webp-600x300-ezgif com-webp-to-jpg-converter](https://github.com/inuwamobarak/TikTok-depth-anything/assets/65142149/2012bcc8-f504-4d44-9d95-a7071ee706b7)

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Acknowledgements](#acknowledgements)

## Introduction

The web application leverages TikTok's "Depth Anything" model, a state-of-the-art monocular depth estimation (MDE) model. It utilizes Flask as the web framework to provide a user-friendly interface for generating depth estimations.

## Setup

1. **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd depth-estimation-webapp-flask
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**
    - For Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - For Linux/Mac:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask App:**
    ```bash
    python app.py
    ```

2. Open your web browser and visit `http://localhost:5000` to access the Depth Estimation WebApp.

3. Upload an image or provide an image URL to generate the depth estimation. Download the generated depth image using the provided button.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for rendering pages.
- `static/`: Includes static files such as stylesheets.
- `depth_estimation.py`: Depth estimation functionality and integration.
- `requirements.txt`: List of project dependencies.
- `images`
- `notebooks`

## Dependencies

- Flask
- Pillow
- NumPy

Install dependencies using the command:
```bash
pip install -r requirements.txt

## Running Docker container(run command in the terminal):

docker build -t depth-estimation-app .
docker run -p 5000:5000 depth-estimation-app

## Acknowledgements

This project utilizes TikTok's "Depth Anything" model. Special thanks to TikTok and the collaborating institutions for open-sourcing the model.
