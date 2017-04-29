To run the application:

1) Start the AMI for UCB MIDS W205 EX2-FULL (ami-d4dd4ec3)
   and log on as root.

2) Attach an EBS volume of sufficient size for your needs.

3) Mount the directory /data on the volume, for example:
   >> mount -t ext4 /dev/xvdf /data

4) Start postgres:  
   >> /data/postgres_start.sh

5) Install packages:
   >> pip install psycopg2
   >> pip install tweepy

6) Change to w205 user
   >> su - w205

7) Enter the Postgres CLI and create a database called "tcount"
   >> psql -U postgres
   postgres=# CREATE DATABASE tcount;
   postgres=# \q

8) Navigate to /data/

9) Clone the repository

10) Navigate to the directory called /EXtweetwordcount/tweetwordcount/
    (Currently in the hw_dev branch)

11) Run the application:
    >> sparse run
  
