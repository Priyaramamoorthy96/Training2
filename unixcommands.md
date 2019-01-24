# Unix
## Install ubuntu in docker

Run the following to get the ubuntu to be installed
 
 -  docker run -it ubuntu bash
 
     ```docker exec -it festive_elion bash ```

## Unix commands

#### - ls --- lists your files.

 ```ls```    
```bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  pramati  proc  root  run  sbin  srv  sys  tmp  usr  var```

- **ls -l --- lists your files in 'long format'** -  ``` ls -l ```

``` OUTPUT
total 8
-rw-r--r-- 1 root root 69 Jan 23 09:10 employee
-rw-r--r-- 1 root root 69 Jan 23 09:08 employee2
```

#### ls -a --- lists all files, including the ones whose filenames begin in a dot, which you do not always want to see. 

root@d7e3573d5eb5:/pramati# ls -a

.  ..  employee  employee2

#### mkdir dirname --- make a new directory

root@d7e3573d5eb5:/pramati# mkdir company

root@d7e3573d5eb5:/pramati# ls

Company  employee  employee2

#### cd dirname --- change directory.

root@d7e3573d5eb5:/pramati# cd company

root@d7e3573d5eb5:/pramati/company#

#### pwd --- tells you where you path

root@d7e3573d5eb5:/pramati/company# pwd

/pramati/company

#### touch --- to create a file

root@d7e3573d5eb5:/pramati/company# touch employee_details

root@d7e3573d5eb5:/pramati/company# ls

employee_details

#### vi --- to write or edit file

 - 1.To use vi in ubuntu docker 
   - docker exec -it containername  bash

 - 2.Then run the following commands
   - apt-get update
   - apt-get install vim
    

#### cat --- to show the content of the file

root@d7e3573d5eb5:/pramati/company# cat employee_details

Name : priya

Age  : 21

DOB  : 11/11/1996

Salary : 3.75l


#### cat file1 >file 2 - over write the content

root@d7e3573d5eb5:/pramati# cat employee>employee1

root@d7e3573d5eb5:/pramati# cat employee1

name:prasanna

age:21

dob:12/12/1997

salary:3.75l

position:Assosiate

#### cat file1>>file2 - append the content

root@d7e3573d5eb5:/pramati# cat employee>>employee1

root@d7e3573d5eb5:/pramati# cat employee1

name:priya

age:21

dob:12/12/1997

salary:3.75l

position:Assosiate

name:priya

age:21

dob:12/12/1997

salary:3.75l

position:Assosiate

#### mv filename1 filename2 --- moves a file 

root@d7e3573d5eb5:/pramati# mv employee1 company

root@d7e3573d5eb5:/pramati# ls

company  employee2

root@d7e3573d5eb5:/pramati# cd company

root@d7e3573d5eb5:/pramati/company# ls

employee1  employee_details

#### cp filename1 filename2 --- copies a file

root@d7e3573d5eb5:/pramati/company# cp employee_details employee_personal_details 

root@d7e3573d5eb5:/pramati/company# cat employee_personal_details

Name : priya

Age  : 21

DOB  : 11/11/1996

Salary : 3.75l

### rm filename --- removes a file.

root@d7e3573d5eb5:/pramati/company# rm employee_personal_details

root@d7e3573d5eb5:/pramati/company# ls

employee_details  pramati

 
### diff filename1 filename2 --- compares files, and shows where they differ

root@d7e3573d5eb5:/pramati/company# diff employee employee

root@d7e3573d5eb5:/pramati/company# diff employee employee_details

1,4c1,5

< Name  :  prasanna

< Age   : 25

< DOB   :12/12/1993

< Salary: 31k


< Name : priya

< Age  : 21

< DOB  : 11/11/1996

< Salary : 3.75l

#### wc filename --- tells you how many lines, words, and characters there are in a file

root@d7e3573d5eb5:/pramati/company# wc employee

 4 10 59 employee

#### date - tells the current date

root@d7e3573d5eb5:/pramati/company# date

Thu Jan 24 05:20:26 UTC 2019

#### find - The find command all of the files within a directory and its subdirectories that match a set of conditions. 

root@d7e3573d5eb5:/pramati# find company

company

company/employee

company/employee_details

company/pramati
