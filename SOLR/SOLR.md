### SOLR
Solr makes it easy for programmers to develop sophisticated, high-performance search applications with advanced features 

#### INSTALLING SOLR 
- JRE - You will need the Java Runtime Environment (JRE) version 1.8 or higher.
- Solr is available from the Solr website at http://lucene.apache.org/solr/.
- For Linux/Unix/OSX systems, download the .tgz file. For Microsoft Windows systems, download the .zip file.

When getting started, all you need to do is extract the Solr distribution archive to a directory of your choosing. When you’re ready to setup Solr for a production environment, please refer to the instructions provided on the Taking Solr to Production page.
To keep things simple for now, extract the Solr distribution archive to your local home directory, for instance on Linux, do:
```
cd ~/
tar zxf solr-x.y.z.tgz
```
Once extracted, you are now ready to run Solr using the instructions provided in the Running Solr section.
#### RUNNING SOLR
##### 1. Start the Server
- If you didn’t start Solr after installing it, you can start it by running bin/solr from the Solr directory.
```
bin/solr start
```
 - If you are running Windows, you can start Solr by running bin\solr.cmd instead.
```
bin\solr.cmd start
```
- This will start Solr in the background, listening on port 8983.

- When you start Solr in the background, the script will wait to make sure Solr starts correctly before returning to the command line prompt.
```
The bin/solr and bin\solr.cmd
```
#### 2. Start Solr with a Different Port
- To change the port Solr listens on, you can use the -p parameter when starting, such as:
```
bin/solr start -p 8984
```
#### 3. Stop Solr

When running Solr in the foreground (using -f), then you can stop it using Ctrl-c. However, when running in the background, you should use the stop command, such as:
```
bin/solr stop -p 8983
```




