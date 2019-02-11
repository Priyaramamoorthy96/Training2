#### Installing Java
- To get started, we'll update our package list:
```
sudo apt-get update
```
- Next, we'll install OpenJDK, the default Java Development Kit on Ubuntu 16.04.
```
sudo apt-get install default-jdk
```
- Once the installation is complete, let's check the version.
```
java -version
```
#### Installing Hadoop
```
wget https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz.mds
```
we'll use the tar command with the -x flag to extract, -z to uncompress, -v for verbose output, and -f to specify that we're extracting from a file. Use tab-completion or substitute the correct version number in the command below:
```
tar -xzvf hadoop-2.7.3.tar.gz
```
Finally, we'll move the extracted files into /usr/local, the appropriate place for locally installed software. Change the version number, if needed, to match the version you downloaded.
```
sudo mv hadoop-2.7.3 /usr/local/hadoop
```
With the software in place, we're ready to configure its environment.

#### Configuring Hadoop's Java Home
Hadoop requires that you set the path to Java, either as an environment variable or in the Hadoop configuration file.
To find the default Java path
```
readlink -f /usr/bin/java | sed "s:bin/java::"
```
To begin, open hadoop-env.sh:
```
sudo nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```
#### Running Hadoop
Now we should be able to run Hadoop:
```
/usr/local/hadoop/bin/hadoop
```
