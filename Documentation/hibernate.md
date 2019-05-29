#### HIBERNATE
Hibernate is a Java framework that simplifies the development of Java application to interact with the database. It is an open source, lightweight, ORM (Object Relational Mapping) tool. Hibernate implements the specifications of JPA (Java Persistence API) for data persistence.
The Hibernate architecture includes many objects such as persistent object, session factory, transaction factory, connection factory, session, transaction etc.

##### The Hibernate architecture
The Hibernate architecture is categorized in four layers.
- Java application layer
- Hibernate framework layer
- Backhand api layer
- Database layer

##### Elements of Hibernate Architecture
For creating hibernate application, the elements of Hibernate architecture plays an important role. They are as follows:
- SessionFactory
The SessionFactory is a factory of session and client of ConnectionProvider. It holds second level cache (optional) of data. The org.hibernate.SessionFactory interface provides factory method to get the object of Session.
- Session
The session object provides an interface between the application and data stored in the database. It is a short-lived object and wraps the JDBC connection. It is factory of Transaction, Query and Criteria. It holds a first-level cache (mandatory) of data. The org.hibernate.Session interface provides methods to insert, update and delete the object. It also provides factory methods for Transaction, Query and Criteria.
- Transaction
The transaction object specifies the atomic unit of work. It is optional. The org.hibernate.Transaction interface provides methods for transaction management.
- ConnectionProvider
It is a factory of JDBC connections. It abstracts the application from DriverManager or DataSource. It is optional.
- TransactionFactory
It is a factory of Transaction. It is optional.

#### Procedure to create a Hibernate Application

The Following are the steps to create Hibernate
- Create the Persistent class
- Create the mapping file for Persistent class
- Create the Configuration file
- Create the class that retrieves or stores the persistent object
- Load the jar file
- Run the first hibernate application by using command prompt
1) Create the Persistent class
- A simple Persistent class should follow some rules:
- A no-arg constructor: It is recommended that you have a default constructor at least package visibility so that hibernate can create the instance of the Persistent class by newInstance() method.
- Provide an identifier property: It is better to assign an attribute as id. This attribute behaves as a primary key in database.
- Declare getter and setter methods: The Hibernate recognizes the method by getter and setter method names by default.
- Prefer non-final class: Hibernate uses the concept of proxies, that depends on - The persistent class. The application programmer will not be able to use proxies for lazy association fetching.
2) Create the mapping file for Persistent class
The mapping file name conventionally, should be class_name.hbm.xml. There are many elements of the mapping file.
- hibernate-mapping : It is the root element in the mapping file that contains all the mapping elements.
- class : It is the sub-element of the hibernate-mapping element. It specifies the Persistent class.
- id : It is the subelement of class. It specifies the primary key attribute in the class.
- generator : It is the sub-element of id. It is used to generate the primary key. There are many generator classes such as assigned, increment, hilo, sequence, native etc. We will learn all the generator classes later.
- property : It is the sub-element of class that specifies the property name of the Persistent class.
3) Create the Configuration file
The configuration file contains information about the database and mapping file. Conventionally, its name should be hibernate.cfg.xml .
4) Create the class that retrieves or stores the object
In this class, we are simply storing the employee object to the database.
5) Load the jar file
For successfully running the hibernate application, you should have the hibernate5.jar file.



