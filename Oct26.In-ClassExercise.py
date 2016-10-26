def main():
   imp_db
   schema = raw_input("Please enter the name of the schema: ")
   table = raw_input("Please enter the name of the table: ")

def bc_query:

    q2 = "select a.name, count(*), count(*)/avg(st_area(a.the_geom)) as density from "+schema+"."+table+" b, exercises.bc_municipality a where ST_contains(a.the_geom, b.the_geom) group by a.name"

def imp_db:
    import psycopg2
    con = psycopg2.connect(database='fall2016', user='class', password='geog4560', host='sql.webdmap.com' , port = '5432')
    cur = con.cursor()
    cur.execute(q2)
    res = cur.fetchall()


fOj = open(r'c:\temp\counties.csv', 'w')
fOj.write("name, state, pop2000, household, x, y, sex ratio, \n")
#r represents every item in the list and t represets every tuple in each item
for r in res:
    l = ""
    for t in r:
        l = l + str(t) + ","
    fOj.write(l.rstrip(",") + "\n")