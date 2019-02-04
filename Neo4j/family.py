from neo4j.v1 import GraphDatabase
uri = "bolt://localhost:7687"
userName = "neo4j"
password = "PILLOWS112012;"
graphDB_Driver = GraphDatabase.driver(uri, auth=(userName, password)) 
cqlNodeQuery = "MATCH (x:Family) RETURN x"
cqlEdgeQuery = "MATCH (x:Family {name:'jack'})-[r]->(y:Family) RETURN y.name,r.Relation"
cqlCreate = """CREATE (Ron:Family{ name: "Ron"}),
(Jack:Family { name: "Jack"}),
(Hermonine:Family { name: "Hermonine"}),
(Rose:Family { name: "Rose"}),
(Ron)-[:Father{Relation:"Father"}]->(Rose),
(Ron)-[:Father {Relation:"Father"}]->(Jack),
(Ron)-[:Husband {Relation:"Husband"}]->(Hermonine),
(Hermonine)-[:Mother {Relation:"Mother"}]->(Rose),
(Hermonine)-[:Mother {Relation:"Mother"}]->(Jack),
(Hermonine)-[:Wife {Relation:"Wife"}]->(Ron),
(Jack)-[:Son {Relation:"son"}]->(Ron),
(Jack)-[:Son {Relation:"son"}]->(Hermonine),
(Jack)-[:Brother {Relation:"Brother"}]->(Rose),
(Rose)-[:Daughter {Relation:"Daughter"}]->(Ron),
(Rose)-[:Daughter {Relation:"Daughter"}]->(Hermonine),
(Rose)-[:Sister {Relation:"Sister"}]->(Jack)"""

with graphDB_Driver.session() as graphDB_Session:
    graphDB_Session.run(cqlCreate)
    nodes = graphDB_Session.run(cqlNodeQuery)
    print("List of family members :")
    for node in nodes:
        print(node)
    nodes = graphDB_Session.run(cqlEdgeQuery)  
    for node in nodes:
       print(node)

