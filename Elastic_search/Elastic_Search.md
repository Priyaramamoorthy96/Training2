### Elasticsearch
Elasticsearch can be downloaded directly from elastic.co in zip, tar.gz, deb, or rpm packages. For Ubuntu, it's best to use the deb (Debian) package which will install everything you need to run Elasticsearch.
##### 1. Downloading and Installing Elasticsearch
- Download the latest Elasticsearch version, which is 2.3.1 at the time of writing.
```
wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.3.1/elasticsearch-2.3.1.deb
```
- Then install it in the usual Ubuntu way with dpkg.

```
sudo systemctl enable elasticsearch.service
```
- To make sure Elasticsearch starts and stops automatically with the server, add its init script to the default runlevels.

```
sudo systemctl enable elasticsearch.service
```

##### 2. Configuring Elasticsearch
- To start editing the main elasticsearch.yml configuration file with nano or your favorite text editor.
```
sudo nano /etc/elasticsearch/elasticsearch.yml
```
- Remove the # character at the beginning of the lines for cluster.name and node.name to uncomment them, and then update their values. Your first configuration changes in the /etc/elasticsearch/elasticsearch.yml file should look like this:
```
. . .
cluster.name: mycluster1
node.name: "My First Node"
path.data: /priya/Mytest/
. . .
```
- Once you make all the changes, save and exit the file. Now you can start Elasticsearch for the first time.
```
sudo systemctl start elasticsearch
```

### Kibana Installation :
- Install Kibana : ```sudo apt install kibana```
- Start kibana service : ```sudo systemctl enable kibana || sudo systemctl start kibana```
- Set password for kibana : ```echo "kibanaadmin:`openssl passwd -apr1`" | sudo tee -a /etc/nginx/htpasswd.users```
### Example:
```
curl -X POST 'http://localhost:9200/tutorial/helloworld/1' -d '{ "message": "Hello World!" }'
OUTPUT :
{"_index":"tutorial","_type":"helloworld","_id":"1","_version":1,"_shards":{"total":2,"successful":1,"failed":0},"created":true}
```
- Check Health : ```curl -X GET "localhost:9200/_cat/health?v```
- List all nodes : ```curl -X GET "localhost:9200/_cat/nodes?v"```
- Display all index : ```curl -X GET "localhost:9200/_cat/indices?v"```
- Create a index : ```curl -X PUT "localhost:9200/customer?pretty"curl -X GET "localhost:9200/_cat/indice```
- Index and Query : ```curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H``` ```'Content-Type: application/json' -d'``````{"name": "John Doe"Index and Query}```
- Retire the doc : ```curl -X GET "localhost:9200/customer/_doc/1?pretty"```
- Delete the doc : ```curl -X DELETE "localhost:9200/customer?pretty"``` ```curl -X GET "localhost:9200/_cat/indices?v"```
- Indexing/Replacing Document : ```curl -X PUT``` ```"localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'``` ```{"name": "Jane Doe"}'```

