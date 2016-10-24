import psycopg2


con = psycopg2.connect(database='fall2016', user='class', password='geog4560', host='sql.webdmap.com' , port = '5432')
cur = con.cursor()
cur.execute("select st_area(st_buffer(the_geom,500)) from exercises.bc_municipality")
res = cur.fetchall()
#print res [0][3]

#prints a list of tuples
for x in res:
    print x

#prints county and state name
#for x in res:
    #print x[2]+", "+x[3]