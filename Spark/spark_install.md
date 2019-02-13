#### Steps to install Spark
Step 1 : Ensure if Java is installed
Before installing Spark, Java is a must have for your system. Following command will verify the version of Java-
```
$java -version
```
If Java is already installed on your system, you get to see the following output which is as follows:
```
java version "1.7.0_71"
```
Java(TM) SE Runtime Environment (build 1.7.0_71-b13)

Java HotSpot(TM) Client VM (build 25.0-b02, mixed mode)
If java is not installed on your system, then install it.

Step 2 : Ensure if Scala is installed

Installing Scala language is mandatory before installing Spark as it is important for implementation. Following command will verify the version of Scala –

Scala language is used to implement Spark. So verify the Scala installation by using following command.

```
$scala -version
```
If Scala application is already installed on your system, you get to see the following response on the screen as shown below:

Scala code runner version 2.11.6 — Copyright 2002-2013, LAMP/EPFL

If you don’t have Scala, then install it.

Step 3 : Download Scala

Download the latest version of Scala. We are currently using scala-2.11.6 version. After downloading, you will be able to find the Scala tar file in the download folder.

Download the current version of Scala where you can find its tar file in the downloads folder.

Step 4 : Install Scala

Follow the given steps to install Spark –

Extract the Scala tar file using following command –
```
$ tar xvf scala-2.11.6.tgz
```
Move Scala software files by using the following commands for moving the Scala software files, to its respective directory (/usr/local/scala).
```
$ su –
Password:

# cd /home/Hadoop/Downloads/

# mv scala-2.11.6 /usr/local/scala

# exit
Set PATH for Scala using following command –
$ export PATH = $PATH:/usr/local/scala/bin
It is very important to verify the installation of Scala once again.
$scala -version
```
If you have Scala, then it returns following response-

Scala code runner version 2.11.6 — Copyright 2002-2013, LAMP/EPFL

Step 5 : Downloading Apache Spark

After finishing with the installation of Java and Scala, Download the latest version of Spark by visiting following command –
```
spark-1.3.1-bin-hadoop2.6 version
```
After this you can find a Spark tar file in the download folder.

Step 6 : Installing Spark

Follow the below steps given below for installing Spark.

Extracting Spark tar file using following command –
```
$ tar xvf spark-1.3.1-bin-hadoop2.6.tgz
```
Move Spark software files to respective directory using following commands –
/usr/local/spark
Configure the environment for Spark
Add the following line to ~/.bashrc file which will add the location, where the spark software files are located to the PATH variable type.

export PATH = $PATH:/usr/local/spark/bin

Use the following below command for sourcing the ~/.bashrc file.
```
$ source ~/.bashrc
```
Step 7 : Verify the Installation of Spark application on your system

Following command will open Spark shell application version.
```
$spark-shell
```


