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
### Example:
```
curl -X POST 'http://localhost:9200/tutorial/helloworld/1' -d '{ "message": "Hello World!" }'
OUTPUT :
{"_index":"tutorial","_type":"helloworld","_id":"1","_version":1,"_shards":{"total":2,"successful":1,"failed":0},"created":true}


curl -X GET "localhost:9200/_cat/health?v" health
curl -X GET "localhost:9200/_cat/nodes?v" list 
curl -X GET "localhost:9200/_cat/indices?v" All indices
curl -X PUT "localhost:9200/customer?pretty"
curl -X GET "localhost:9200/_cat/indices?v"       create a index
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
 "name": "John Doe"	Index and Query
}
curl -X GET "localhost:9200/customer/_doc/1?pretty"	to retive the docs
curl -X DELETE "localhost:9200/customer?pretty"
curl -X GET "localhost:9200/_cat/indices?v" to delete the docs
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d' Indexing/Replacing Document
{
 "name": "Jane Doe"
}
'
curl -X POST "localhost:9200/customer/_doc/1/_update?pretty" -H 'Content-Type: application/json' -d'
{
 "doc": { "name": "Jane Doe" } update docs
}
'
```
