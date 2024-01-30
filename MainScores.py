from flask import Flask, render_template
from Score import ScoreManager

app = Flask(__name__)


@app.route('/')
def display_score():
    try:
        with open(ScoreManager().file_name, 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    return render_template('score_template.html', score=current_score)


@app.route('/score')
def score_server():
    try:
        with open(ScoreManager().file_name, 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    html_response = (f"<html><head><title>User Score</title></head>"
                     f"<body><h1>The user's score is: {current_score}</h1></body></html>")
    return html_response


if __name__ == '__main__':
    app.run(debug=True)
