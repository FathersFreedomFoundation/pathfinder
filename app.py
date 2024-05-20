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

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    property_address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(20))
    property_type = db.Column(db.String(50))
    listing_date = db.Column(db.DateTime)
    zestimate = db.Column(db.Float)
    last_contact_date = db.Column(db.DateTime)
    contact_status = db.Column(db.String(50))
    communications = db.relationship('Communication', backref='lead', lazy=True)
    offers = db.relationship('Offer', backref='lead', lazy=True)
class PropertyDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Float)
    square_feet = db.Column(db.Integer)
    lot_size = db.Column(db.Float)
    year_built = db.Column(db.Integer)
    last_sold_price = db.Column(db.Float)
    last_sold_date = db.Column(db.DateTime)
    condition = db.Column(db.String(200))
    additional_features = db.Column(db.Text)
class Communication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    direction = db.Column(db.String(10))
    medium = db.Column(db.String(50))
    content = db.Column(db.Text)
    response_expected = db.Column(db.Boolean)
    response_received = db.Column(db.Boolean)
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    offer_price = db.Column(db.Float)
    offer_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    expiration_date = db.Column(db.DateTime)
    offer_status = db.Column(db.String(50))
class UserAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))
    action_type = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
