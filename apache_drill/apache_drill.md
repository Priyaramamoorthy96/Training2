#### APACHE DRILL

#### INSTALLATION :
Java Installation Prerequisite Check
Run the following command in a terminal (Linux and Mac OS X) or Command Prompt (Windows) to verify that Java 8 is the version in effect:
```
java -version
```
The output looks something like this:
```
java version "1.8.0"
```
Java(TM) SE Runtime Environment (build 1.8.0_7965-b15)
Java HotSpot(TM) 64-Bit Server VM (build 24.79-b02, mixed mode)
Install Drill on Linux or Mac OS X

Complete the following steps to install Drill:
- In a terminal window, change to the directory where you want to install Drill.
Download the latest version of Apache Drill here or from the Apache Drill mirror site with the command appropriate for your system:
```
wget http://apache.mirrors.hoobly.com/drill/drill-1.15.0/apache-drill-1.15.0.tar.gz
curl -o apache-drill-1.15.0.tar.gz
```
- Extract the contents of the Drill .tar.gz file. Use sudo if necessary:
```
tar -xvzf <.tar.gz file name>
```
- The extraction process creates an installation directory containing the Drill software.
- At this point, you can start Drill.
- Start Drill on Linux and Mac OS X
```
cd apache-drill-<version>
```
- Issue the following command to launch Drill in embedded mode:
```
bin/drill-embedded
```
- The message of the day followed by the 0: jdbc:drill:zk=local> prompt appears.


#### OPERATIONS IN DRILL :
- OR:

QUERY :
0: jdbc:drill:zk=local> select * from  dfs.`/home/priyadharshini/priya/Mytest/example2.json` where mark1=60 or mark2=60 or mark3=60;

OUTPUT :
+------+-------+------+---------+-----------+--------+--------+--------+-------------------+----------+
|  ID  | name  | age  | gender  | standard  | mark1  | mark2  | mark3  |       addr        | pincode  |
+------+-------+------+---------+-----------+--------+--------+--------+-------------------+----------+
| 001  | Adam  | 12   | male    | six       | 70     | 50     | 60     | 23 new street     | 111222   |
| 003  | Bob   | 12   | male    | six       | 60     | 80     | 70     | 10 cross street   | 111222   |
| 005  | Esha  | 12   | female  | six       | 70     | 60     | 65     | 20 garden street  | 111222   |
+------+-------+------+---------+-----------+--------+--------+--------+-------------------+----------+
3 rows selected (0.123 seconds)

- LIKE:

QUERY :
0: jdbc:drill:zk=local> select * from  dfs.`/home/priyadharshini/priya/Mytest/example2.json` where  addr like '2%';

OUTPUT :
+------+--------+------+---------+-----------+--------+--------+--------+-------------------+----------+
|  ID  |  name  | age  | gender  | standard  | mark1  | mark2  | mark3  |       addr        | pincode  |
+------+--------+------+---------+-----------+--------+--------+--------+-------------------+----------+
| 001  | Adam   | 12   | male    | six       | 70     | 50     | 60     | 23 new street     | 111222   |
| 005  | Esha   | 12   | female  | six       | 70     | 60     | 65     | 20 garden street  | 111222   |
| 006  | Ganga  | 12   | female  | six       | 100    | 95     | 98     | 25 north street   | 111222   |
| 007  | Jack   | 13   | male    | six       | 55     | 45     | 45     | 2 park street     | 111222   |
| 008  | Leena  | 12   | female  | six       | 90     | 85     | 95     | 24 south street   | 111222   |
+------+--------+------+---------+-----------+--------+--------+--------+-------------------+----------+
5 rows selected (0.262 seconds)

- ORDER BY :

QUERY :
0: jdbc:drill:zk=local> select * from  dfs.`/home/priyadharshini/priya/Mytest/example2.json` orderby  mark3; (ERROR - give space)

OUTPUT :
0: jdbc:drill:zk=local> select * from  dfs.`/home/priyadharshini/priya/Mytest/example2.json` order by  mark3;
+------+--------+------+---------+-----------+--------+--------+--------+--------------------+----------+
|  ID  |  name  | age  | gender  | standard  | mark1  | mark2  | mark3  |        addr        | pincode  |
+------+--------+------+---------+-----------+--------+--------+--------+--------------------+----------+
| 002  | Amit   | 12   | male    | six       | 40     | 50     | 40     | 12 old street      | 111222   |
| 007  | Jack   | 13   | male    | six       | 55     | 45     | 45     | 2 park street      | 111222   |
| 001  | Adam   | 12   | male    | six       | 70     | 50     | 60     | 23 new street      | 111222   |
| 005  | Esha   | 12   | female  | six       | 70     | 60     | 65     | 20 garden street   | 111222   |
| 003  | Bob    | 12   | male    | six       | 60     | 80     | 70     | 10 cross street    | 111222   |
| 004  | David  | 12   | male    | six       | 50     | 70     | 70     | 15 express avenue  | 111222   |
| 010  | Peter  | 13   | female  | six       | 80     | 85     | 88     | 16 park avenue     | 111222   |
| 009  | Mary   | 13   | female  | six       | 75     | 85     | 90     | 5 west street      | 111222   |
| 008  | Leena  | 12   | female  | six       | 90     | 85     | 95     | 24 south street    | 111222   |
| 006  | Ganga  | 12   | female  | six       | 100    | 95     | 98     | 25 north street    | 111222   |
+------+--------+------+---------+-----------+--------+--------+--------+--------------------+----------+
10 rows selected (0.476 seconds)

- SUM :

QUERY :
0: jdbc:drill:zk=local> select sum(mark1) from  dfs.`/home/priyadharshini/priya/Mytest/example2.json`;

OUTPUT :
+---------+
| EXPR$0  |
+---------+
| 690     |
+---------+

- COUNT :

QUERY ;
0: jdbc:drill:zk=local> select count(mark1) from  dfs.`/home/priyadharshini/priya/Mytest/example2.json` where mark1>60;

OUTPUT :
+---------+
| EXPR$0  |
+---------+
| 6       |
+---------+









