import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)

BASE_URL = "https://api.api-ninjas.com/v1/quotes"
API_KEY = os.getenv('API_KEY')

def getQuote():
    response = requests.get(BASE_URL, headers={'X-Api-Key': API_KEY}).json()

    quote = response[0]['quote']
    author = response[0]['author']
    category = response[0]['category']

    return quote, author, category

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote, author, category = getQuote()
        return render_template("index.html", quote=quote, author=author, category=category)
    else: return render_template("index.html", quote="", author="", category="")

if __name__ == '__main__':
    app.run()
