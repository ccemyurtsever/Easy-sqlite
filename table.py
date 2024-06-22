import sqlite3 as sql

def table(DatabaseName, TableName, **kwargs):
    try:
        conn = sql.connect(f'{DatabaseName}.db')
        cursor = conn.cursor()
        
        columns = ""
        for column_name, column_type in kwargs.items():
            columns += f"{column_name} {column_type}, "
        
        columns = columns.rstrip(", ")
        
        create_table = f"""CREATE TABLE IF NOT EXISTS {TableName} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            {columns}
                        );"""
        cursor.execute(create_table)
        conn.commit()
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False
    finally:
        conn.close()

# table('xxx', 'xxxxx', name='TEXT NOT NULL', email='TEXT NOT NULL', password='TEXT NOT NULL')
