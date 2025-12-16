import sqlite3

def load_to_db(rows, db_path="users.db"):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            phone_number TEXT,
            address TEXT,
            signup_date TEXT
        )
    """)

    insert_query = """
        INSERT INTO users (
            user_id,
            name,
            email,
            phone_number,
            address,
            signup_date
        ) VALUES (?, ?, ?, ?, ?, ?)
    """

    for row in rows:
        try:
            cursor.execute(insert_query, (
                row["user_id"],
                row["name"],
                row["email"],
                row["phone_number"],
                row["address"],
                row["signup_date"]
            ))
        except sqlite3.IntegrityError:
            continue

    connection.commit()
    connection.close()
