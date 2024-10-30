from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# init app & db connect
app = Flask(__name__)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://learnflaskapi_noisefrom:4972a1de9365f5ad01f1c556c4ee9484a970c082@he-h2.h.filess.io:3305/learnflaskapi_noisefrom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()
