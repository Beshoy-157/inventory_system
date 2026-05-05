from utils.db import init_db
from services.system import System
from models.product import Product

# 🔧 init DB
init_db()

system = System()

# 👤 admin
system.add_admin("admin", "1234")
system.login("admin", "1234")


def menu():
    print("\n========= MENU =========")
    print("1- Add Stock")
    print("2- Sell")
    print("3- Show Stock")
    print("4- Reports")
    print("5- 🔍 Search")
    print("6- 🧾 Transactions")
    print("7- Exit")


def get_int(msg):
    while True:
        try:
            val = int(input(msg))
            if val < 0:
                print("❌ Enter positive number")
                continue
            return val
        except:
            print("❌ Enter a valid number")


while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        name = input("Product name: ")
        qty = get_int("Quantity: ")
        system.add_stock(Product(name), qty)

    elif choice == "2":
        name = input("Product name: ")
        qty = get_int("Quantity: ")
        system.sell_product(Product(name), qty)

    elif choice == "3":
        system.inventory.show_stock()

    elif choice == "4":
        system.show_reports()

    elif choice == "5":
        name = input("Search product: ")
        system.search(name)

    elif choice == "6":
        system.inventory.show_transactions()

    elif choice == "7":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice")