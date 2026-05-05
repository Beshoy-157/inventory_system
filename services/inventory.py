from utils.db import connect

class Inventory:

    def add_product(self, product, qty):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT qty FROM products WHERE name=?", (product.name,))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE products SET qty=? WHERE name=?",
                (result[0] + qty, product.name)
            )
        else:
            cursor.execute(
                "INSERT INTO products (name, qty) VALUES (?, ?)",
                (product.name, qty)
            )

        cursor.execute(
            "INSERT INTO transactions (name, qty, type) VALUES (?, ?, ?)",
            (product.name, qty, "IN")
        )

        conn.commit()
        conn.close()

    def remove_product(self, product, qty):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT qty FROM products WHERE name=?", (product.name,))
        result = cursor.fetchone()

        if result and result[0] >= qty:
            cursor.execute(
                "UPDATE products SET qty=? WHERE name=?",
                (result[0] - qty, product.name)
            )

            cursor.execute(
                "INSERT INTO transactions (name, qty, type) VALUES (?, ?, ?)",
                (product.name, qty, "OUT")
            )

        conn.commit()
        conn.close()

    def get_stock(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT name, qty FROM products")
        data = cursor.fetchall()

        conn.close()

        return {name: qty for name, qty in data}

    def get_transactions(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT name, qty, type FROM transactions")
        data = cursor.fetchall()

        conn.close()

        return data