from flask import Flask, render_template, redirect, url_for, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = Flask(__name__, template_folder='pages')

MONGO_URI = 'mongodb+srv://database_owner:DatabasePassword@cluster0.ep9zacz.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(MONGO_URI, server_api = ServerApi('1'))
db = client.flashcards
collection = db.flashcards


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/flashcards')
def display_flashcards():
    # Display blank flashcards for now
    flashcards = [
                {
            'shanghainese': 'Shanghainese',
            'phonetics': 'Phonetics',
            'english': 'English'
        },
        {
            'shanghainese': 'Shanghainese',
            'phonetics': 'Phonetics',
            'english': 'English'
        },
        {
            'shanghainese': 'Shanghainese',
            'phonetics': 'Phonetics',
            'english': 'English'
        },
        {
            'shanghainese': 'Shanghainese',
            'phonetics': 'Phonetics',
            'english': 'English'
        }
    ]  

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
