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






