from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('landing.html')

@app.route('/get_message', methods=['GET'])
def get_message():
    message = "Code Genrated for the dataset!!"
    return jsonify({'message': message})