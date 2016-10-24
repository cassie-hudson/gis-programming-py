import psycopg2


con = psycopg2.connect(database='fall2016', user='class', password='geog4560', host='sql.webdmap.com' , port = '5432')
cur = con.cursor()
cur.execute("select * from county where state_name = 'Texas'")
res = cur.fetchall()
print res



a = (5 ,6 ,7)
b = [9, 10, 11]

print a, b;

print a[0]
print b [0]

c = [(1,2), (3,4), (5,6)]

print c[0]

print c[0][0]

print c[0][1]

for i in range (0,3):
    print a[i]

for i in a:
    print i

for i in c:
    print i

for i in c:
    print i[1]

for i in c:
    print i[1], 1[0]

