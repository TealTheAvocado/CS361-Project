from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__, template_folder='pages')

MONGO_URI = "mongodb+srv://database_owner:DatabasePassword@cluster0.ep9zacz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client['flashcards']

DATABASE_PASSWORD = "123123123"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/go_to_home')
def go_to_home():
    return redirect(url_for('index'))


@app.route('/go_to_about')
def go_to_about():
    return redirect(url_for('about'))


@app.route('/manage_database', methods=['GET', 'POST'])
def manage_database():
    if request.method == 'POST':
        password = request.form['password']

        if password == DATABASE_PASSWORD:
            # Database management code here
            return redirect(url_for('add_data'))

    return render_template('manage_database.html')


@app.route('/add_data', methods=['POST'])
def add_data():
    if request.method == 'POST':
        shanghainese = request.form.get('shanghainese')
        phonetics = request.form.get('phonetics')
        english = request.form.get('english')
        category = request.form.get('category')
        return "Data added successfully"

    return render_template('add_data.html')

@app.route('/database')
def show_database():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)

    # Choose the database and collection
    db = client['flashcards']
    collection = db['flashcards']  # Replace with your collection name

    # Query MongoDB to retrieve the records
    database_records = list(collection.find({}))

    # Close the MongoDB connection
    client.close()

    return render_template('database.html', database_records=database_records)


if __name__ == '__main__':
    app.run(debug=True)
