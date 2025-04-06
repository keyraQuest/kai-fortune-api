from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Kai Fortune API is live. Use /fortune to get a random fortune."

@app.route('/fortune')
def fortune():
    with open('kai_fortunes.txt', 'r') as f:
        fortunes = f.readlines()
    return random.choice(fortunes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
