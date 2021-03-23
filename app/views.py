"""
Application routes definitions
"""
from flask import Flask, request, render_template, jsonify
from app.manager import BotAnswer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parser', methods=['POST'])
def parser():
    """
    Extract location from userInput.
    Returns formatted userInput, api response, coordinates for the map
    """
    userInput = request.form.get("question")
    routeReturn = BotAnswer(userInput).response
    return routeReturn


if __name__ == "__main__":
    app.run()
