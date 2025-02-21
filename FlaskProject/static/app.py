
from flask import Flask, render_template, request,jsonify
import json
app = Flask(__name__)
CONFIG_FILE = "serverK1.json"

@app.route("/get_config", methods=["GET"])

@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/json')
def load_data():
    with open('serverK1.json', 'r', encoding='utf-8') as file:
        _serverK1 = json.load(file)
    return _serverK1

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run(debug=False)
