# https://www.javatpoint.com/flask-session

from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = 'vinod'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['Username'] = request.form['Username']
        session['Password'] = request.form['Password']
    return render_template('profile.html')


@app.route('/logout')
def logout():
    session.pop('Username')
    session.pop('Password')
    return "The User is signed out"


@app.route('/profile', methods=['GET'])
def profile():
    print(session)
    if session and 'vinod' in session['Username']:
        return render_template('success.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)