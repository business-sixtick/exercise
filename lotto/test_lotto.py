import sqlite3
import pandas as pd
#conn =  sqlite3.connect('../data/lotto.db') #C:\source\exercise\data\lotto.db
conn =  sqlite3.connect('C:\source\exercise\data\lotto.db') #C:\source\exercise\data\lotto.db
cursor = conn.cursor()
rows = cursor.execute('select * from win').fetchall()

pass # TODO

accumulate = {}
for row in rows :
    # print(row)
    for i in row[1:-1] :
        # print(i)
        if not accumulate.get(i) :
            accumulate[i] = 0
        accumulate.update({i : accumulate.get(i) + 1})

print(len(accumulate), accumulate)
keys =  sorted(accumulate.keys())
for i in keys :
    # print(i, accumulate.get(i))
    pass

conn.close()