from flask import Flask, render_template, request, redirect
from utils.db import init_db
from services.system import System
from models.product import Product
import os

app = Flask(__name__)

# init DB
init_db()

system = System()
system.add_admin("admin", "1234")
system.login("admin", "1234")


# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ADD STOCK
# =========================
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    qty = int(request.form["qty"])

    system.add_stock(Product(name), qty)
    return redirect("/")


# =========================
# SELL PRODUCT
# =========================
@app.route("/sell", methods=["POST"])
def sell():
    name = request.form["name"]
    qty = int(request.form["qty"])

    system.sell_product(Product(name), qty)
    return redirect("/")


# =========================
# STOCK
# =========================
@app.route("/stock")
def stock():
    data = system.inventory.get_stock()
    return {"stock": data}


# =========================
# TRANSACTIONS
# =========================
@app.route("/transactions")
def transactions():
    data = system.inventory.get_transactions()
    return {"transactions": data}


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)