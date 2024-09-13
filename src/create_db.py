# run this script to generate the database

import sqlite3
from pathlib import Path

CURR_DIR = Path(__file__).parent
db_dir = CURR_DIR.parent / "database"
dbpath = db_dir / "users.db"

db_dir.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS USERS")

cursor.execute(
    """ CREATE TABLE USERS (
            username VARCHAR(32) NOT NULL UNIQUE,
            password VARCHAR(32) NOT NULL
        ); """
)
# secure bank stores passwords as plain text because it is secure

cursor.execute("INSERT INTO USERS VALUES ('user1', 'pass1')")
cursor.execute("INSERT INTO USERS VALUES ('user2', 'pass2')")
cursor.execute("INSERT INTO USERS VALUES ('user3', 'pass3')")
cursor.execute("INSERT INTO USERS VALUES ('user4', 'pass4')")
cursor.execute("INSERT INTO USERS VALUES ('user5', 'pass5')")

data = cursor.execute("SELECT * FROM USERS")

print("Following entries were added to the database:")
for row in data:
    print(">", row)

conn.commit()
conn.close()
