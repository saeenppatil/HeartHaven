from flask import Flask, jsonify, request, render_template
import requests 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)