# Dice Roller Application

This is a simple dice roller application built with FastAPI for the backend and HTML/JavaScript for the frontend. The app simulates rolling a dice, displaying a random number from 1 to 6, and dynamically generating dice images.

## Features
- Roll a dice and generate a random number (1-6).
- Dynamically generate dice images using Python's Pillow library.
- Frontend interface with a roll button and dice display.

## Project Structure
```
Project Root
├── api.py              # Backend code for the dice roll
├── index.html          # Frontend file for the dice roll interface
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel configuration
├── static/             # Static assets (CSS, JS, Images)
│   ├── style.css       # Styling for the frontend
│   ├── script.js       # Frontend JavaScript (if separated from HTML)
│   └── images/         # Images used in the project
└── README.md           # Documentation for the project
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server locally:
   ```bash
   uvicorn api:app --reload
   ```

4. Open the `index.html` file in a browser to interact with the dice roller.

## Deployment
This project is configured to be deployed on [Vercel](https://vercel.com/). Simply run the following command to deploy:
```bash
vercel
```
