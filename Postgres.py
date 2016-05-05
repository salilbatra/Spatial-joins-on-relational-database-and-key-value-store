import psycopg2
import time, os
conn = psycopg2.connect(database='postgis_22_DBSpatial', user='postgres', password='salilbatra', host='127.0.0.1', port='5432')
#print("opened database very very successfully")


cur = conn.cursor()
start = time.time()
#print(datetime.time)
cur.execute("""SELECT ng.name, cs.latitude, cs.longitude
                        FROM "neighborhoods" AS ng, "collisions" AS cs
                           WHERE ST_Contains(ng.geom,cs.geom);""")

cur.execute("""SELECT ng.name, cs.latitude, cs.longitude
                FROM "neighborhoods" AS ng, "collisions" AS cs
                    WHERE _ST_Contains(ng.geom,cs.geom);""")

cur.execute("""SELECT ng.name, cs.latitude, cs.longitude
                FROM "neighborhoods" AS ng, "collisions" AS cs
                WHERE ST_Intersects(ng.geom,cs.geom);""")

cur.execute("""SELECT ng.name, cs.latitude, cs.longitude
                FROM "neighborhoods" AS ng, "collisions" AS cs
                    WHERE _ST_Intersects(ng.geom,cs.geom);""")
#cur.execute("""SELECT ng.geom FROM "neighborhoods" as ng WHERE ng.name = 'SOMERTON'""")
end = time.time()-start

for row in cur.fetchall():
    print(row)
print(end)