import psycopg2

conn = psycopg2.connect(user = "postgres", password = "iwasbornfree", host = "127.0.0.1", database = "luck")
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