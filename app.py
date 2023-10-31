from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='pages')

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

if __name__ == '__main__':
    app.run(debug=True)