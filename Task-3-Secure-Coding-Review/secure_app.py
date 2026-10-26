
"""
CodeAlpha Cybersecurity Internship
Task 3: Secure Coding Review

Demonstration of secure SQL query handling.
"""

import sqlite3


def find_user(username):
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            role TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO users (username, role) VALUES (?, ?)",
        ("alice", "user")
    )
    cursor.execute(
        "INSERT INTO users (username, role) VALUES (?, ?)",
        ("admin", "administrator")
    )

    # Secure: parameterized SQL keeps input separate from the query.
    query = "SELECT username, role FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    results = cursor.fetchall()

    print("Reviewing user lookup...")
    for row in results:
        print(f"Username: {row[0]}, Role: {row[1]}")

    connection.close()


if __name__ == "__main__":
    name = input("Enter username to search: ")
    find_user(name)