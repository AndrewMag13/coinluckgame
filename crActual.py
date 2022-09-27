from postgresso import *
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS actual(
    id         SERIAL PRIMARY KEY NOT NULL,
    userid     INTEGER,
    username   TEXT,
    link       TEXT,
    UNIQUE     ("userid"));
    """)
conn.commit()
conn.close()