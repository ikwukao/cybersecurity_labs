# Critical section with row-level locking
with sqlite3.connect("database.sqlite") as conn:
    conn.execute("BEGIN IMMEDIATE")  # Exclusive lock
    cursor = conn.cursor()
    cursor.execute("SELECT stock FROM items WHERE id = ? FOR UPDATE", (item_id,))
    stock = cursor.fetchone()[0]

    if stock > 0:
        cursor.execute("UPDATE items SET stock = stock - 1 WHERE id = ?", (item_id,))
        conn.commit()
        # Safe - no race possible
