from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# --- Function to load data from JSON file ---
def load_json_data():
    with open("products.json") as f:
        return json.load(f)

# --- Function to load data from CSV file ---
def load_csv_data():
    data = []
    with open("products.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert ID to int and price to float if needed
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            data.append(row)
    return data

# --- Main route ---
@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    data = []
    error = None

    # Handle invalid source
    if source == "json":
        if not os.path.exists("products.json"):
            error = "JSON file not found."
        else:
            data = load_json_data()
    elif source == "csv":
        if not os.path.exists("products.csv"):
            error = "CSV file not found."
        else:
            data = load_csv_data()
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if not error and product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if int(item["id"]) == product_id]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template("product_display.html", products=data, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)