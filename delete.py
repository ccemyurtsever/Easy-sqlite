import sqlite3 as sql
import os

def delete_DB(DatabaseName):
    try:
        db_path = f'{DatabaseName}.db'
        if os.path.exists(db_path):
            os.remove(db_path)
            return True
        else:
            print("Null")
    except Exception as e:
        print(f"Error: {e}")


def deleteTable(DatabaseName, TableName):
    try:
        conn = sql.connect(f'{DatabaseName}.db')
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE {TableName}")
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

