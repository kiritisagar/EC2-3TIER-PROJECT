from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:sagarmunna@localhost/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def home():
    return jsonify(message='Welcome to the Backend API!')

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify(users=[user.name for user in users])

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)

