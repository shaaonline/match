
# Image Matching Platform

## Features
- Upload two images to compare.
- Displays differences using a heatmap.

## Setup Instructions

1. Install Python 3.9+ and Git.
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```bash
    python app.py
    ```
4. Open `http://localhost:5000` in your browser.

## Deployment on Heroku

1. Install the Heroku CLI.
2. Log in to Heroku:
    ```bash
    heroku login
    ```
3. Create a new Heroku app and push the code:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    heroku create
    git push heroku master
    ```
4. Open the app:
    ```bash
    heroku open
    ```
