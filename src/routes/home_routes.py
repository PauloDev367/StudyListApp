from flask import jsonify, render_template, request, redirect, url_for
from src.data.db_context import app
from src.services.user_service import UserService

user_service = UserService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('user/register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    user_service.create_user(username, email, password)

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    user = user_service.login_user(email, password)
    if user:
        print(f"User {user.username} logged in successfully.")
        return redirect('/containers')
    print("Login failed. Invalid email or password.")
    return redirect('/')