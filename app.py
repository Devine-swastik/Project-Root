from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def dice():
    dice_num = random.randint(1, 6)
    return render_template('index.html', dice=dice_num)

# Vercel compatibility
def handler(event, context):
    from flask import request
    return app(request.environ, start_response=lambda status, headers: None)
