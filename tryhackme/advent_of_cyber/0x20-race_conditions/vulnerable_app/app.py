from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)""")
    # Seed data
    c.execute("INSERT OR REPLACE INTO items VALUES (1, 'SleighToy Limited Edition', 1)")
    c.execute("INSERT OR REPLACE INTO items VALUES (2, 'Bunny Plush (Blue)', 1)")
    conn.commit()
    conn.close()


@app.route("/checkout", methods=["POST"])
def checkout():
    item_id = request.json["item_id"]

    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("SELECT stock FROM items WHERE id = ?", (item_id,))
    stock = c.fetchone()[0]

    if stock > 0:
        c.execute("UPDATE items SET stock = stock - 1 WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()

        # Check for negative stock flags
        if stock - 1 < 0:
            if item_id == 1:
                return jsonify({"message": "Flag: THM{WINNER_OF_R@CE007}"})
            elif item_id == 2:
                return jsonify({"message": "Flag: THM{WINNER_OF_BUNNY_R@CE}"})

        return jsonify({"status": "success", "stock": stock - 1})

    conn.close()
    return jsonify({"status": "out of stock"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
