# author: Hayden Johnston
# date: 08/20/2023
# description: SQLite implementation for GPT-3 chat memory

import sqlite3

def connect_db():
    """Connects to sqlite database."""
    try:
        con = sqlite3.connect('bot.db')
    except:
        print("database.db connection failed")
    finally:
        return con

def create_table():
    """Creates a table in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS memory ("
                    "id TEXT NOT NULL, "
                    "memory TEXT NOT NULL)")

        con.commit()
        print("User table created.")
    except:
        print("Table creation failed")
    finally:
        con.close()

def insert_memory(data):
    """Add a new user to database."""
    con = connect_db()
    cur = con.cursor()
    data['memory'] = to_string(data['memory'])
    try:
        cur.execute("INSERT or IGNORE into memory (id, memory) VALUES (?, ?)",
                    (data['id'], data['memory']))
        con.commit()
        con.rollback()
    except:
        print("Unable to add to database.")
    finally:
        con.close()

def get_all():
    """Get all users from the table."""
    items = []
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM my_table")
        database_data = cur.fetchall()

        for data in database_data:
            dict = {"id": data[0], "memory": data[1]}
            items.append(dict)

    except:
        print("Error: unable to fetch database")
    finally:
        con.close()
    return items

def get_by_id(id):
    """Get user memory by id."""
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute(f"SELECT * FROM memory WHERE id= ?;",(id,))
        row = cur.fetchall()
    except:
        print("get memory by id failed")
    finally:
        con.close()
        return row

def update_memory(data):
    """Update memory in the database."""
    try:
        con = connect_db()
        cur = con.cursor()
        data['memory'] = to_string(data['memory'])
        cur.execute("UPDATE memory SET memory = ? WHERE id = ?",
                    (data['memory'], data['id']))
        con.commit()
    except Exception as e:
        print("update database failed", str(e))
    finally:
        con.close()

def delete_memory(id):
    """Delete a user memory from the database."""
    try:
        con = connect_db()
        con.execute("DELETE FROM memory WHERE id = ?",
                    (id,))
        con.commit()
    except:
        print("Unable to delete memory.")
    finally:
        con.close()

def to_string(memory: list) -> str:
    """Convert list to string"""
    return ", ".join(memory)

def to_list(memory: str) -> list:
    """Convert string to list"""
    return memory.split(", ")
