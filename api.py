from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import random
from PIL import Image, ImageDraw

app = FastAPI()

# Allow CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

def generate_dice_image(number, output_path):
    """
    Generate a dice image with the given number and save it as a PNG file.
    :param number: The number on the dice (1-6).
    :param output_path: The path to save the image.
    """
    if number < 1 or number > 6:
        raise ValueError("Dice number must be between 1 and 6")

    # Create a square white canvas for the dice
    img_size = 200
    dice_color = (255, 255, 255)
    border_color = (0, 0, 0)
    dot_color = (0, 0, 0)

    img = Image.new("RGB", (img_size, img_size), dice_color)
    draw = ImageDraw.Draw(img)

    # Draw the border of the dice
    border_thickness = 10
    draw.rectangle(
        [(0, 0), (img_size - 1, img_size - 1)], outline=border_color, width=border_thickness
    )

    # Positions for dots
    positions = {
        1: [(100, 100)],  # Center
        2: [(50, 50), (150, 150)],  # Top-left, Bottom-right
        3: [(50, 50), (100, 100), (150, 150)],  # Top-left, Center, Bottom-right
        4: [(50, 50), (50, 150), (150, 50), (150, 150)],  # Four corners
        5: [(50, 50), (50, 150), (150, 50), (150, 150), (100, 100)],  # Four corners + Center
        6: [(50, 50), (50, 100), (50, 150), (150, 50), (150, 100), (150, 150)],  # Two vertical rows
    }

    dot_radius = 15
    for pos in positions[number]:
        x, y = pos
        draw.ellipse(
            [(x - dot_radius, y - dot_radius), (x + dot_radius, y + dot_radius)],
            fill=dot_color,
        )

    # Save the image to the specified output path
    img.save(output_path)
    print(f"Dice image with number {number} saved at {output_path}")


@app.get("/roll_dice")
def roll_dice():
    """
    Roll a dice and return the result as an integer (1-6).
    """
    dice_value = random.randint(1, 6)
    return {"dice_value": dice_value}


@app.get("/dice_image/{number}")
def get_dice_image(number: int):
    """
    Generate and return a dice image based on the number (1-6).
    """
    if number < 1 or number > 6:
        return {"error": "Invalid dice number. Must be between 1 and 6."}

    # Generate the dice image
    file_path = f"dice_{number}.png"
    generate_dice_image(number, file_path)

    # Serve the image file
    return FileResponse(file_path)
