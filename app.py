from flask import Flask, render_template, request,jsonify
import json
app = Flask(__name__)
CONFIG_FILE = "static/serverK1.json"

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template("index.html")
@app.route('/serverK1.json',methods=['GET'])
def load_data():
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
            _serverK1 = json.load(file)
        return jsonify(_serverK1)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

