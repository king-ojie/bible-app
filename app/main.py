from flask import Flask, render_template
import requests
from transformers import pipeline
import random

app = Flask(__name__)

# Load Hugging Face sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to get a random Bible verse
def get_random_bible_verse():
    # Using a free Bible API (example: labs.bible.org)
    api_url = "https://labs.bible.org/api/?passage=random&type=json"
    response = requests.get(api_url)
    if response.status_code == 200:
        verse_data = response.json()[0]
        return f"{verse_data['bookname']} {verse_data['chapter']}:{verse_data['verse']} - {verse_data['text']}"
    return "John 3:16 - For God so loved the world..."

# Function to generate a short message based on sentiment
def generate_message(verse):
    sentiment = sentiment_analyzer(verse)[0]
    if sentiment['label'] == 'POSITIVE':
        return "This verse brings hope and joy!"
    else:
        return "A thoughtful reminder to reflect."

@app.route('/', methods=['GET', 'POST'])
def index():
    verse = get_random_bible_verse()
    message = generate_message(verse)
    return render_template('index.html', verse=verse, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)