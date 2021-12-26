from db import get_db


def insert_user(name, last_name, user_name, email):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(name, last_name, user_name, email) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [name, last_name, user_name, email])
    db.commit()
    return True


def update_user(name, last_name, user_name, email):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE users SET name = ?, last_name = ?, email = ? WHERE user_name = ?"
    cursor.execute(statement, [name, last_name, user_name, email])
    db.commit()
    return True


def delete_user(user_name):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE user_name = ?"
    cursor.execute(statement, [user_name])
    db.commit()
    return True


def get_by_user_name(user_name):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, last_name, user_name, email FROM users WHERE user_name = ?"
    cursor.execute(statement, [user_name])
    return cursor.fetchone()


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, last_name, user_name, email FROM users"
    cursor.execute(query)
    return cursor.fetchall()