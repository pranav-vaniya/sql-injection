# run this script to read the contents of the database

import sqlite3
from pathlib import Path

CURR_DIR = Path(__file__).parent
dbpath = CURR_DIR.parent / "database" / "users.db"

conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

data = cursor.execute("SELECT * FROM USERS")

print("The USERS table contains the following entries:")
for row in data:
    print(">", row)

conn.close()
