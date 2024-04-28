from flask import Flask, jsonify, request, render_template
import requests 
from backend import logistic_function

app = Flask(__name__)

data_storage = []

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/api/params', methods=['POST'])
def receive_data():
    data = request.get_json()  # Extract JSON data from request
    print("Received data:", data)  # Debug print to console
    data_storage.append(data)  # Append data to the storage
    return jsonify({"status": "success", "received_data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

def parseDataIntoArray(data):
    return [
        data['age'],
        data['bmi'],
        data['sex'],
        data['attack'],
        data['stroke'],
        data['diabetes'],
        data['high blood cholesterol levels'],
        data['cigarettes'],
        data['alcholic'],
        data['difficulty'],
        data['physical'],
        data['fruit'],
        data['vegetables'],
        

    ]
