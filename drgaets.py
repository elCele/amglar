import sqlite3
import re

# 1. Carica il dump MySQL
with open("amglar_clean.sql", "r", encoding = "utf-8") as f:
    sql_script = f.read()

# 2. Ripulisci il dump per renderlo compatibile con SQLite
sql_script = re.sub(r"SET .*?;\n", "", sql_script)            # rimuovi SET
sql_script = re.sub(r"START TRANSACTION;\n", "", sql_script)  # rimuovi START TRANSACTION
sql_script = re.sub(r"COMMIT;\n", "", sql_script)             # rimuovi COMMIT
sql_script = re.sub(r" COMMENT '.*?'", "", sql_script)        # rimuovi COMMENT
sql_script = re.sub(r" ENGINE=.*?;", ";", sql_script)         # rimuovi ENGINE=InnoDB ecc.
sql_script = re.sub(r"/\*![0-9]+.*?\*/;", "", sql_script, flags=re.DOTALL)  # rimuovi /*! ... */

# 3. Crea il database SQLite e applica lo script
conn = sqlite3.connect("amglar.db")
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()

# 4. Controlla se la tabella è stata creata
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tabelle trovate:", tables)

conn.close()
