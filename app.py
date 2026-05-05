from flask import Flask, render_template, request, redirect, session
from utils.db import init_db
from services.system import System
from models.product import Product
import os

app = Flask(__name__)
app.secret_key = "secret_key_123"

# init db
init_db()

# system
system = System()
system.add_admin("admin", "1234")


# =========================
# LOGIN
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if system.login(username, password):
            return redirect("/dashboard")

    return render_template("login.html")


# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    stock = system.inventory.get_stock()
    transactions = system.inventory.get_transactions()

    total_products = len(stock)
    total_quantity = sum(stock.values())
    total_transactions = len(transactions)

    return render_template(
        "dashboard.html",
        total_products=total_products,
        total_quantity=total_quantity,
        total_transactions=total_transactions
    )


# =========================
# ADD STOCK
# =========================
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    qty = int(request.form["qty"])

    system.add_stock(Product(name), qty)
    return redirect("/dashboard")


# =========================
# SELL PRODUCT
# =========================
@app.route("/sell", methods=["POST"])
def sell():
    name = request.form["name"]
    qty = int(request.form["qty"])

    system.sell_product(Product(name), qty)
    return redirect("/dashboard")


# =========================
# STOCK PAGE
# =========================
@app.route("/stock")
def stock():
    data = system.inventory.get_stock()
    return render_template("stock.html", data=data)


# =========================
# TRANSACTIONS PAGE
# =========================
@app.route("/transactions")
def transactions():
    data = system.inventory.get_transactions()
    return render_template("transactions.html", data=data)


# =========================
# RUN SERVER (FOR RENDER + LOCAL)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)