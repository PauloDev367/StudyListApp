from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../views', static_folder='../../assets')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'minha-chave-secreta-muito-longa-e-dificil-de-adivinhar'

db = SQLAlchemy(app)