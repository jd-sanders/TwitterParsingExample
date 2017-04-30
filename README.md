## Application Overview

Tweetwordcount is an application that uses an Apache Storm topology to analyze the word content of tweets coming from Twitter’s streaming API in real time. As tweets occur, the application ingests the tweets, parses the text into individual words, and keeps an ongoing count of words across all content. A PostgreSQL database is used to store the word counts as they are updated.

## Architecture and Apache Storm

This application is designed to run on Amazon Elastic Compute (EC2) instance. A public machine image, the UCB MIDS W205 EX2- FULL, has been developed and shared with the necessary technology (Storm, Python, and Postgres).

Storm topologies consist of spouts, whose function is to generate streams of data, and bolts the process the data, potentially sending it to additional bolts. The application tweetwordcount has a single spout component, Tweets-spout, which uses the Tweepy library in Python to connect to the Twitter API and ingest the content of tweets. There are two bolt components, parse-bolt and wordcount-bolt. The Parse bolt accepts tweets from the tweet spout, and parses into individual words, which are then sent to the wordcount bolt. The wordcount bolt tallies the individual words and updates the Postgres database.

It is possible to have multiple instances of each spout or bolt. The original recommendation for this topology was to have three spouts, three parse bolts, and two word count bolts. However, the topology appears to run more error free with a simpler topology of one spout, and two each of each bolt.

## File Descriptions

**config.json**: Sets system configuration variables for Apache Storm

**fabfile.py**, pass.py: These file defines custom actions to be performed before and after the submission of topologies. In this case, the remain blank.

**project.clj**: Additional project variables definitions

**/src/bolts/Tweets.py**: The Python process that connect to the Twitter streaming API and ingests tweets.

**/src/spouts/parse.py**: The Python process that parses tweet content.

**/src/spouts/wordcount.py**: The Python process that counts words and updates a Postgres database.

**/topologies/tweetwordcount.clj**: A Clojure file defining the Storm topology

## Dependencies

The Storm topology in this application is written in Clojure, and the processing units are written in Python. The python classes use the packages tweepy and psycopg2. The data is stored in a PostgreSQL database.

## To run the application:

1. Start the AMI for UCB MIDS W205 EX2-FULL (ami-d4dd4ec3) and log on as root.

2. Attach an EBS volume of sufficient size for your needs.

3. Mount the directory /data on the volume, for example:

   ` >> mount -t ext4 /dev/xvdf /data`

4. Start postgres:  

   ` >> /data/postgres_start`

5. Install packages:

   ```
   >> pip install psycopg2
   >> pip install tweepy
   ```

6. Change to w205 user

   `>> su - w205`

7. Enter the Postgres CLI and create a database called "tcount"
   
   ```
   >> psql -U postgres
   >> postgres=# CREATE DATABASE tcount;
   >>postgres=# \q
   ```

8. Navigate to /data/

9. Clone the repository, and modify the tweets.py file to include a valid set of Twitter credentials

10. Navigate to the directory called /EXtweetwordcount/tweetwordcount/ (Currently in the hw_dev branch)

11. Run the application:

    ` >> sparse run`

