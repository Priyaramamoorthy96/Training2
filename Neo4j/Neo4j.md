###     Neo4j
### Installation
- Neo4j is implemented in Java, so you’ll need to have the Java Runtime Environment (JRE) installed. 
```
sudo apt install default-jre default-jre-headless 
```
- First we’ll add the repository key to our keychain.
```
wget --no-check-certificate -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
```
- Then add the repository to the list of apt sources.
```
echo 'deb http://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
```
- Finally update the repository information and install Neo4j.
```
sudo apt update
sudo apt install neo4j
```
- The server should have started automatically and should also be restarted at boot. If necessary the server can be stopped with
```
sudo service neo4j stop
```
- Restarted with
```
sudo service neo4j start
```
### Accessing Neo4j
- Link to dataserver - http://localhost:7474/browser/.
- Give username and password (neo4j and neo4j)
### Neo4j CQL 
- To create a node
```
Syntax  : CREATE (node_name); 
Example : CREATE(name);
```
- To create node with properties
```
Syntax : CREATE (node:label { key1: value, key2: value, . . . . . . . . .  });
Example : CREATE (Lily:info{name: "Lily", DOB: 1985, Location: "Chennai"});
```
- To return the created Node
```
Syntax : CREATE (Node:Label{properties. . . . }) RETURN Node 
Example : CREATE (Lily:info{name: "Lily", DOB: 1985, Location: "Chennai"}) return Lily
```
- To create a relationship
```
Syntax : CREATE (node1)-[:RelationshipType]->(node2) 
Example : 
CREATE (Lily:info{name: "Lily", DOB: 1985, Location: "Chennai"})
CREATE (Ind:Country {name: "India"})
CREATE (Lily)-[r:Citizen]->(Ind) 
```
- Creating a Relationship Between the Existing Nodes
```
Syntax :
MATCH (a:LabeofNode1), (b:LabeofNode2) 
   WHERE a.name = "nameofnode1" AND b.name = " nameofnode2" 
CREATE (a)-[: Relation]->(b) 
RETURN a,b 
Example:
MATCH (a:info), (b:Country) WHERE a.name = "Lily" AND b.name = "India" 
CREATE (a)-[r: Citizen]->(b) 
RETURN a,b 
```
- Creating a Relationship with Label and Properties
```
Syntax :
CREATE (node1)-[label:Rel_Type {key1:value1, key2:value2, . . . n}]-> (node2) 
EXample:
MATCH (a:info), (b:Country) WHERE a.name = "Lily" AND b.name = "India" 
CREATE (a)-[r:BATSMAN_OF {Age:35, Education:BE}]->(b)  
RETURN a,b 
```
- To Delete the node
```
Syntax :
MATCH (node:label {properties . . . . . . . . . .  }) 
DETACH DELETE node
EXample:
MATCH (lily:info {name: "lily", DOB: 1988, POB: "Delhi"}) 
DETACH DELETE lily
```









