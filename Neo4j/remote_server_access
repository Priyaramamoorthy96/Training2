### Connect to the remote server from browser 
The following changes should be done in the neo4j.conf, inorder to connect to the remote server from browser

```
UMCOMMENT : dbms.connectors.default_listen_address=0.0.0.0

dbms.connector.bolt.enabled=true
#dbms.connector.bolt.tls_level=OPTIONAL
#dbms.connector.bolt.listen_address=:7687
dbms.connector.bolt.listen_address=0.0.0.0:7687

dbms.connector.http.enabled=true
#dbms.connector.http.listen_address=:7474
dbms.connector.http.listen_address=0.0.0.0:7474

dbms.connector.https.enabled=true
#dbms.connector.https.listen_address=:7473
dbms.connector.https.listen_address=0.0.0.0:7473

```
