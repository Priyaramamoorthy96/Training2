# POSTGRESQL

## POSTGRESQL 

PostgreSQL (pronounced "post-gress-Q-L") is an open source relational database management system ( DBMS ) developed by a worldwide team of volunteers. PostgreSQL is not controlled by any corporation or other private entity and the source code is available free of charge.

### Installation of PostgreSql

There are three steps to complete the PostgreSQL installation:

 1.Download PostgreSQL installer for Windows

 2.Install PostgreSQL

 3.Verify the installation
 
 ### Installation of PostgreSql in docker
 
   - docker run --name postgres -e POSTGRES_PASSWORD=tiger -d postgres
    
   - docker exec -it postgres psql -U postgres 
 

### Connecting to a PostgreSql Database

 There 2 ways to connect
 
  - Psql(Interactive SQL shell terminal) 
     
  - PgAdmin(GUI)

## Operations in PostgreSql

### 1.Create Database

Create Database database_name;
 
Create Database pramati;
    

### 2. Select Database
  
- To see all the Databases   -  \l

- To select a database       -  \c pramati;  [c - connect]

- To Disconnect the database -  \q


### 3. Drop Database

Drop database database_name;

Drop database pramati;


### 4. Create Table

- create table tablename( col 1 datatype,col 1 datatype,...);

- create table employee(id int primary key not null, name text not null,age int not null,salary real);

- Description of the table - \d 

    - output:

      List of relations

 Schema |   Name   | Type  |  Owner

--------+----------+-------+----------

 public | employee | table | postgres


### To exit from postgresql

TO Come out of postgresql - ctrl + c




  






