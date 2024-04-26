from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pathfinder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: to disable a feature which will be removed in future versions.

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the Flask app and the SQLAlchemy db
migrate = Migrate(app, db)

# Your model definitions (tables for your database) will go below here

@app.route('/')
def home():
    return 'Hello, Pathfinder!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
