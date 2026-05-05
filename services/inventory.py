from utils.db import connect

class Inventory:

    # ➕ ADD
    def add_product(self, product, qty):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT qty FROM products WHERE name=?", (product.name,))
        result = cursor.fetchone()

        if result:
            new_qty = result[0] + qty
            cursor.execute(
                "UPDATE products SET qty=? WHERE name=?",
                (new_qty, product.name)
            )
        else:
            cursor.execute(
                "INSERT INTO products (name, qty) VALUES (?, ?)",
                (product.name, qty)
            )

        # transaction IN
        cursor.execute(
            "INSERT INTO transactions (name, qty, type) VALUES (?, ?, ?)",
            (product.name, qty, "IN")
        )

        conn.commit()
        conn.close()

    # ➖ SELL
    def remove_product(self, product, qty):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT qty FROM products WHERE name=?", (product.name,))
        result = cursor.fetchone()

        if result and result[0] >= qty:
            new_qty = result[0] - qty

            cursor.execute(
                "UPDATE products SET qty=? WHERE name=?",
                (new_qty, product.name)
            )

            # transaction OUT
            cursor.execute(
                "INSERT INTO transactions (name, qty, type) VALUES (?, ?, ?)",
                (product.name, qty, "OUT")
            )

        conn.commit()
        conn.close()

    # 📦 STOCK
    def get_stock(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT name, qty FROM products")
        data = cursor.fetchall()

        conn.close()

        return {name: qty for name, qty in data}

    # 🧾 TRANSACTIONS
    def get_transactions(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT name, qty, type FROM transactions")
        data = cursor.fetchall()

        conn.close()

        return data