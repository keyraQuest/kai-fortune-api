from flask import Flask
import random

app = Flask(__name__)

@app.route("/fortune")
def get_fortune():
    with open("kai_fortunes.txt", "r") as f:
        fortunes = f.readlines()
    fortune = random.choice(fortunes).strip()
    return fortune

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)