from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=None)

    try:
        if source == 'json':
            data = read_json('products.json')
        else:
            data = read_csv('products.csv')
    except Exception as e:
        return render_template('product_display.html', error="Failed to read data", products=None)

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found", products=None)
        except ValueError:
            return render_template('product_display.html', error="Invalid ID", products=None)

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)