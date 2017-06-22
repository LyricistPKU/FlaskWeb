# -*- encoding=UTF-8 -*-
from flask import Flask
# from application import views, modules
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)

