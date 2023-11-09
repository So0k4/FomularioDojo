from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "any secret string"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["email"] = request.form["email"]
    return redirect(url_for("result"))

@app.route("/result")
def result():
    return render_template("result.html", name=session["name"], email=session["email"])

if __name__ == "__main__":
    app.run(debug=True)