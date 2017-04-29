import sys
import psycopg2


#Connect to database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

# Create a cursor
cur = conn.cursor()

# Execute a select
try:
    cur.execute("SELECT word, count from Tweetwordcount WHERE count >= %s AND count <= %s",(sys.argv[1],sys.argv[2]))
    records = cur.fetchall()
except IndexError:
    print "Please invoke the script with two integers separated by a space"
    quit()
 
# Print the records
for rec in records:
    print rec[0] + ":", rec[1]

# Tidy things up
conn.commit()
conn.close()

