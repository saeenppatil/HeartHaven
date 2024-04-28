from flask import Flask, jsonify, request, render_template
import requests 
from backend import logistic_function

app = Flask(__name__)

data_storage = []
model_data_array = []

def to_int(value):
    return int(float(value))

def ageCategories(age):
    if((age > 17) & (age < 24)):
        return 1
    elif((age > 24) & (age < 29)):
        return 2
    elif((age > 29) & (age < 34)):
        return 3
    elif((age > 34) & (age < 39)):
        return 4
    elif((age > 39) & (age < 44)):
        return 5
    elif((age > 44) & (age < 49)):
        return 6
    elif((age > 49) & (age < 54)):
        return 7
    elif((age > 54) & (age < 59)):
        return 8
    elif((age > 59) & (age < 64)):
        return 9
    elif((age > 64) & (age < 69)):
        return 10
    elif((age > 69) & (age < 74)):
        return 11
    elif((age > 74) & (age < 79)):
        return 12
    else:
        return 13

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/go-survey')
def start_survey():
    return render_template('survey.html')
    
@app.route('/go-landing')
def start_landing():
    return render_template('landing.html')

@app.route('/api/params', methods=['POST'])
def receive_data():
    data = request.get_json()  # Extract JSON data from request
    print("Received data:", data)  # Debug print to console
    data_storage.append(data)  # Append data to the storage

    if data is not None:
        first_name = data.get('first')
        last_name = data.get('last')
        age = data.get('age')
        age_category = ageCategories(int(age))

        model_data_array = [
            to_int(data.get('highBP')),
            to_int(data.get('highChol')),
            to_int(data.get('BMI')),
            to_int(data.get('smoke')),
            to_int(data.get('stroke')),
            to_int(data.get('diabetes')),
            to_int(data.get('physActivity')),
            to_int(data.get('fruit')),
            to_int(data.get('veggies')),
            to_int(data.get('drinking')),
            to_int(data.get('genHealth')),
            to_int(data.get('mentalHealth')),
            to_int(data.get('physHealth')),
            to_int(data.get('difficultyStairs')),
            to_int(data.get('sexOptions')),
            age_category,
        ]

    print(model_data_array)
    return jsonify({"status": "success", "received_data": data}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
