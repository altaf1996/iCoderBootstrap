from flask import Flask, render_template
app = Flask(__name__)



# Home Page
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html") 

# About Page
@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")

# More Page
@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

# Cart Pagr
@app.route("/cart", methods=["POST", "GET"])
def cart():
    return render_template("cart.html")




if __name__ == "__main__":
    app.run(debug=True)