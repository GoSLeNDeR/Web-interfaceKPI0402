from flask import Flask, render_template, request

app = Flask(__name__)

def user_profile(user_id):
    return f"Это профиль пользователя с ID {user_id}"
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run(debug=False)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return 'Вы вошли в систему!'
    else:
        return render_template('index.html')


