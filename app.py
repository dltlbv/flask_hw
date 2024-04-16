from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "Name 1", "age": 1},
    {"name": "Name 2", "age": 2},
    {"name": "Name 3", "age": 3},
]

contacts = [
    {"contact": "Contact 1", "phone": "123-456-7890"},
    {"contact": "Contact 2", "phone": "987-654-3210"},
    {"contact": "Contact 3", "phone": "456-789-0123"},
]

products = [
    {"product": "Product 1", "price": 10},
    {"product": "Product 2", "price": 20},
    {"product": "Product 3", "price": 30},
]


@app.route("/")
def home():
    return render_template("home.html", users=users)


@app.route("/about")
def about():
    return render_template("about.html", products=products)


@app.route("/contact")
def contact():
    return render_template("contact.html", contacts=contacts)


if __name__ == "__main__":
    app.run(debug=True)
