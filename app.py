from flask import Flask, render_template, request, redirect, url_for
from collections import Counter

app = Flask(__name__)

# Global variable to store guesses
guesses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_guess():
    global guesses
    country = request.form['country'].strip().title()
    if country:
        guesses.append(country)
    return redirect(url_for('results'))

@app.route('/results')
def results():
    global guesses
    if guesses:
        count = Counter(guesses)
        most_common = count.most_common(1)[0]
        return render_template('results.html', guesses=count, most_common=most_common)
    return render_template('results.html', guesses={}, most_common=None)

if __name__ == '__main__':
    app.run(debug=True)
