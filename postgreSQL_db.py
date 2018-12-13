import psycopg2 as pg



username="postgres"
conn = pg.connect(dbname=username,user=username,password="Love0419",host="localhost",port=5432)
cur = conn.cursor()
#cur.execute("CREATE TABLE test1 (id integer PRIMARY KEY,name text)")
#cur.execute("INSERT INTO test2 (id,name) VALUES (111111,'Mr Anoun');")
cur.execute("SELECT * FROM test2;")
print (cur.fetchall())
conn.commit()
cur.close()
conn.close()