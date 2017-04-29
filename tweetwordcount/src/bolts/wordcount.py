from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        
        # Open a connection to Postgres
        # This line doesn't seem to create the database
        # Create "tcount" in advance
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # Create a table
        self.cur = self.conn.cursor()
        self.cur.execute('''DROP TABLE IF EXISTS Tweetwordcount''')
        self.cur.execute('''CREATE TABLE Tweetwordcount
                    (word TEXT PRIMARY KEY     NOT NULL,
                     count INT     NOT NULL);''')
        self.conn.commit()

        self.counts = Counter()
        
       

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        count = self.counts[word]

        # Now insert or update the entry in Postgres
        if count is 1:
            self.cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s,%s)", \
                              (word,count))
        else:
            self.cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", \
                              (count, word))
        self.conn.commit()

        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
