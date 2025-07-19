from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    filename = "./data/items.json"
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            items = json.loads(f.read())["items"]
    except (FileNotFoundError, KeyError):
        items = []
    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)