from flask import Flask, render_template, redirect, url_for, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import requests
import random

app = Flask(__name__, template_folder='pages')

MONGO_URI = 'mongodb+srv://database_owner:DatabasePassword@cluster0.ep9zacz.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(MONGO_URI, server_api = ServerApi('1'))
db = client.flashcards
collection = db.flashcards


# Function to connect to MongoDB and retrieve data
def get_data_from_mongodb():
    data = list(collection.find({}))
    return data
def get_data():
    data = get_data_from_mongodb()
    selected_flashcards = random.sample(data, 6)
    flashcards = []
    for item in selected_flashcards:
        flashcard = {
            'shanghainese': item.get('shanghainese', ''),
            'phonetics': item.get('phonetics', ''),
            'english': item.get('english', ''),
            'category': item.get('category', '')
        }
        flashcards.append(flashcard)
    return flashcards  # Return the list directly

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/flashcards', methods=['GET'])
def display_flashcards():
    flashcards = get_data()
    return render_template('flashcards.html', flashcards=flashcards)

@app.route('/database')
def show_database():
    try:
        database_records = collection.find({})
        return render_template('database.html', database_records=database_records)
    except Exception as e:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
