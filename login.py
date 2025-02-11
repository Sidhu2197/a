from flask import Flask, render_template, url_for, flash, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

users = {
    "admin": generate_password_hash("admin123"),
    "test": generate_password_hash("test123")
}

# Add login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Please login first', 'error')
            return redirect(url_for('signin'))
        return f(*args, **kwargs)
    return decorated_function

# Keep existing login route
@app.route("/login", methods=["GET", "POST"])
def login():
    # ...existing code...
    return render_template("login.html")

# Add new signin route
@app.route("/")
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Please fill in all fields", "error")
            return redirect(url_for("signin"))

        stored_password = users.get(username)
        if stored_password and check_password_hash(stored_password, password):
            session["logged_in"] = True
            session["username"] = username
            session.permanent = True
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for("signin"))

    return render_template("signin.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {session.get('username')}!"

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully", "success")
    return redirect(url_for("signin"))

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)