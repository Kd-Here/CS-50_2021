# print(dir(sqlite3))
# https://www.tutorialspoint.com/sqlite/sqlite_quick_guide.htm

import sqlite3


ab = sqlite3.connect('example.db')
nd=ab.cursor()

nd.execute('''CREATE TABLE stocks
(date text, trans text, symbol text, qty real, price real)''')
nd.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
ab.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
ab.close()
