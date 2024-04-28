from flask import Flask, jsonify, request, render_template
import requests 

app = Flask(__name__)

data_storage = []

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
        bmi = data.get('BMI') 
        sex = data.get('sexOptions')
        diseaseOrAttack = data.get('HeartAttack')
        stroke = data.get('stroke')
        diabetes = data.get('diabetes')
        highChol = data.get('highChol')
        smoke = data.get("smoke")
        drink = data.get("drinking")
        diffStairs = data.get("difficultyStairs")
        physActivity = data.get("physActivity")
        fruit = data.get("fruit")
        veggies = data.get("veggies")
        genHealth = data.get("genHealth")
        mentalHealth = data.get("mentalHealth")
        physHealth = data.get("physHealth")
        

    return jsonify({"status": "success", "received_data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)