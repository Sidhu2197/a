from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash("All fields are required!", "danger")
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash("Username already taken. Please choose another.", "warning")
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please use another email.", "warning")
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password)

        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('home'))

    return render_template("register.html")
