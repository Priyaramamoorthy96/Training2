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






