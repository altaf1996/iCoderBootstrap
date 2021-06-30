from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html") 

@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)