from datetime import datetime

from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = "myapp123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "kit.23.19bec068@gmail.com"
app.config["MAIL_PASSWORD"] = "lvyb ylmg jkht zlsz"
db = SQLAlchemy(app)
mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

        date = datetime.strptime(date, "%Y-%m-%d").date()
        form = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        flash("Form is submitted Successfully!", "success")
        message_body = f"Thank you for your submission {first_name}"
        message = Message(subject="New form Submission", sender=app.config["MAIL_USERNAME"], recipients=[email], body=message_body)
        mail.send(message)
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            db.create_all()
            app.run(debug=True, port=5000)


##completed the app