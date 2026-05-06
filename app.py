from flask import Flask, render_template, request, redirect
from utils.db import init_db
from services.system import System
from models.product import Product
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

init_db()

system = System()
system.add_admin("admin", "1234")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if system.login(request.form["username"], request.form["password"]):
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    stock = system.inventory.get_stock()
    transactions = system.inventory.get_transactions()

    return render_template(
        "dashboard.html",
        total_products=len(stock),
        total_quantity=sum(stock.values()),
        total_transactions=len(transactions)
    )


@app.route("/add", methods=["POST"])
def add():
    system.add_stock(Product(request.form["name"]), int(request.form["qty"]))
    return redirect("/dashboard")


@app.route("/sell", methods=["POST"])
def sell():
    system.sell_product(Product(request.form["name"]), int(request.form["qty"]))
    return redirect("/dashboard")


@app.route("/stock")
def stock():
    return render_template("stock.html", data=system.inventory.get_stock())


@app.route("/transactions")
def transactions():
    return render_template("transactions.html", data=system.inventory.get_transactions())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

@app.route("/index")
def index():
    return render_template("index.html")
    return render_template("index.html")