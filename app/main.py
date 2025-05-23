from flask import Flask, render_template, jsonify
import requests
from transformers import pipeline

app = Flask(__name__)


sentiment_analyzer = pipeline("sentiment-analysis")

def get_random_bible_verse():
    api_url = "https://bible-api.com/data/kjv/random"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['random_verse']
    return {
        "book": "John",
        "chapter": 3,
        "verse": 16,
        "text": "For God so loved the world..."
    }

def generate_sentiment(verse_text):
    sentiment = sentiment_analyzer(verse_text)[0]
    if sentiment['label'] == 'POSITIVE':
        return "This verse brings hope and joy!"
    else:
        return "A thoughtful reminder to reflect."

@app.route('/')
def index():
    verse_dict = get_random_bible_verse()
    verse_text = f"{verse_dict['book']} {verse_dict['chapter']}:{verse_dict['verse']} - {verse_dict['text']}"
    sentiment_msg = generate_sentiment(verse_dict['text'])
    return render_template('index.html', verse=verse_text, message=sentiment_msg)

@app.route('/generate')
def generate():
    verse_dict = get_random_bible_verse()
    verse_text = f"{verse_dict['book']} {verse_dict['chapter']}:{verse_dict['verse']} - {verse_dict['text']}"
    sentiment_msg = generate_sentiment(verse_dict['text'])
    return jsonify({"verse": verse_text, "message": sentiment_msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
