import psycopg2

conn = psycopg2.connect(user = "postgres", password = "iwasbornfree", host = "127.0.0.1", database = "luck")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id         SERIAL PRIMARY KEY NOT NULL,
    userid     INTEGER,
    username   TEXT,
    rub        INTEGER,
    mesh       INTEGER,
    vivc       INTEGER,
    plod       REAL,
    plodd      INTEGER,
    ref        INTEGER,
    refco      INTEGER,
    inp        INTEGER,
    outp       INTEGER,
    bon        INTEGER,
    bond       INTEGER,
    course     INTEGER,
    сс1        INTEGER,
    сс         INTEGER,
    lang       TEXT,
    water      INTEGER,
    UNIQUE     ("userid"));
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS fruits(
    id         SERIAL PRIMARY KEY NOT NULL,
    userid     INTEGER,
    straw      INTEGER,
    cher       INTEGER,
    appl       INTEGER,
    banan      INTEGER,
    sliv       INTEGER,
    grape      INTEGER,
    caram      INTEGER,
    caramc     INTEGER,
    pineappl   INTEGER,
    pineapplc  INTEGER,
    drag       INTEGER,
    dragc      INTEGER,
    UNIQUE     ("userid"));
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS req(
    id         SERIAL PRIMARY KEY NOT NULL,
    userid     INTEGER,
    mon        INTEGER,
    app        INTEGER,
    UNIQUE     ("id"));
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
    id         SERIAL PRIMARY KEY NOT NULL,
    userid     INTEGER,
    oirt       TEXT,
    oirv       INTEGER,
    bustak     REAL,
    bustav     INTEGER,
    casit      INTEGER,
    casiv      INTEGER,
    caset      INTEGER,
    casev      INTEGER,
    otv        INTEGER,
    otk        INTEGER,
    otvc       INTEGER,
    otvk       INTEGER,
    UNIQUE     ("userid"));
    """)
conn.commit()
conn.close()

