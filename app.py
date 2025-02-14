
from flask import Flask, render_template, request
import json
app = Flask(__name__)
def load_data():
    with open('serverK1.json', 'r', encoding='utf-8') as file:
        _serverK1 = json.load(file)
    return _serverK1

@app.route('/index')
@app.route('/')
def index():
    data = load_data()  # Загружаем данные из JSON
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run(debug=False)
