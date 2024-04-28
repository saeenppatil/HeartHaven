from flask import Flask, jsonify, request, render_template
import numpy as np
import json
app = Flask(__name__)

data_storage = []
model_data_array = []

# Define coefficients obtained from logistic regression model
coefficients = np.array([0.530747, 0.711591, -0.005263, 0.430810, 1.110706, 0.241793, 0.012939, -0.122841, 0.014835, -0.814256, 0.479267, 0.003791, 0.005063, 0.124037, 0.692602, 0.237020])  # Coefficients for predictor variables

# Define logistic function (sigmoid function)
def logistic_function(x, coefficients):
    z = np.dot(x, coefficients)  # Calculate the weighted sum of predictor variables and coefficients
    return 1 / (1 + np.exp(-z))  # Apply the logistic function to get probability


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

def age_group_chance(age):
    if((age > 17) & (age < 24)):
        return ("18","23","0.51%")
    elif((age > 24) & (age < 29)):
        return ("24","29","0.71%")      
    elif((age > 29) & (age < 34)):
        return ("30","34","1.13%")
    elif((age > 34) & (age < 39)):
        return ("35","39","1.40%")
    elif((age > 39) & (age < 44)):
        return ("40","44","2.17%")
    elif((age > 44) & (age < 49)):
        return ("44","49","3.59%")
    elif((age > 49) & (age < 54)):
        return ("50","54","5.42%")
    elif((age > 54) & (age < 59)):
        return ("55", "59","7.31%")
    elif((age > 59) & (age < 64)):
        return ("60", "64","10.10%")
    elif((age > 64) & (age < 69)):
        return ("65", "69","13.02%")
    elif((age > 69) & (age < 74)):
        return ("70", "74","16.77%")
    elif((age > 74) & (age < 79)):
        return ("75", "79","19.36%")
    else:
        return ("80", "80+","23.96")

@app.route('/')
def index():
    return render_template('landing.html')


# "probability": probabilityOfUserHeartDisease,
# "Name": first_name + " " + last_name,
# "Age": age,
# "AgeGroupLowerBound": ageGroupLowerBound,
# "AgeGroupHigherBound": ageGroupHigherBound,
# "AgeGroupProbability": ageGroupProbability,
@app.route('/go-result/prob/<float:user_prob>/name/<user_name>/age/<int:user_age>/ageLower/<int:age_lower>/ageHigher/<int:age_higher>/ageProb/<age_prob>')
def start_result(user_prob, user_name, user_age, age_lower, age_higher, age_prob):
    data = {
        "probability": user_prob,
        "Name": user_name,
        "Age": user_age,
        "AgeGroupLowerBound": age_lower,
        "AgeGroupHigherBound": age_higher,
        "AgeGroupProbability": age_prob,
    }
    print(data)
    return render_template('result.html', user_data=data)

@app.route('/go-survey')
def start_survey():
    return render_template('survey.html')

@app.route('/css-result')
def start_result_css():
    return render_template('result.css')

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
    probabilityOfUserHeartDisease = logistic_function(model_data_array, coefficients)
    ageGroupLowerBound, ageGroupHigherBound, ageGroupProbability = age_group_chance(int(age))
    response = {
        "status": "success",
        "probability": probabilityOfUserHeartDisease,
        "Name": first_name + " " + last_name,
        "Age": age,
        "AgeGroupLowerBound": ageGroupLowerBound,
        "AgeGroupHigherBound": ageGroupHigherBound,
        "AgeGroupProbability": ageGroupProbability,
    }
    print("\n")
    print(probabilityOfUserHeartDisease)
    print(response)
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)