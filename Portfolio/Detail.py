from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    success_message = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with open("contact_submissions.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        success_message = "✅ Thank you for contacting me! I will get back to you soon."

    return render_template("index.html", message=success_message)

if __name__ == "__main__":
    app.run(debug=True)
