from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/roll_dice")
def roll_dice():
    """
    Roll a dice and return the result as an integer (1-6).
    """
    dice_value = random.randint(1, 6)
    return {"dice_value": dice_value}
