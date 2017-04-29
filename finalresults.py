import sys
import psycopg2

#word = sys.argv[1]
#print type(word)

#Connect to database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# Create a cursor
cur = conn.cursor()

# Execute a select
try:
    cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s",(sys.argv[1],))
    records = cur.fetchall()
except IndexError:
    cur.execute("SELECT word, count from Tweetwordcount ORDER BY word ASC")
    records = cur.fetchall()

# Print the records
for rec in records:
    print rec[0] + ",", rec[1]

# Tidy things up
conn.commit()
conn.close()

