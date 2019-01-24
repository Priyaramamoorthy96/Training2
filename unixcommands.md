# Unix
## Install ubuntu in docker

Run the following to get the ubuntu to be installed
 
 -  docker run -it ubuntu bash
 
     ```docker exec -it festive_elion bash ```

## Unix commands

 - **ls --- Lists your files**

 ```
ls
 
OUTPUT :
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  pramati  proc  root  run  sbin  srv  sys  tmp  usr  var
```

- **Lists your files in 'long format'** 

``` 
Syntax : 
ls -l

Example :
root@d7e3573d5eb5:/pramati#ls -l

Output :
total 8
-rw-r--r-- 1 root root 69 Jan 23 09:10 employee
-rw-r--r-- 1 root root 69 Jan 23 09:08 employee2
```

- **Lists all files, including the ones whose filenames begin in a dot, which you do not always want to see**

```
Syntax :
ls -a

Example:
 root@d7e3573d5eb5:/pramati#ls -a
 
OUTPUT :
.  ..  employee  employee2
```

-  **Make a new directory**
```
Syntax:
mkdir dirname

Example:
root@d7e3573d5eb5:/pramati# mkdir company
root@d7e3573d5eb5:/pramati# ls

OUTPUT :
Company  employee  employee2
```

-  **Change directory.**

```
Syntax :
cd dirname

Example :
root@d7e3573d5eb5:/pramati# cd company

Ouput :
root@d7e3573d5eb5:/pramati/company#
```

- **To get the path**

```
Syntax :
pwd

Example :
root@d7e3573d5eb5:/pramati/company# pwd

Ouput :
/pramati/company
```

- **To create a file**

```
Syntax :
touch filename

Example :
root@d7e3573d5eb5:/pramati/company# touch employee_details
root@d7e3573d5eb5:/pramati/company# ls

Output :
employee_details
````

- **To write or edit file**
```
 - 1.To use vi in ubuntu docker 
   - docker exec -it containername  bash

 - 2.Then run the following commands
   - apt-get update
   - apt-get install vim
   ``` 

- **To show the content of the file**

```
Syntax :
cat filenmame

Example :
root@d7e3573d5eb5:/pramati/company# cat employee_details

Output:
Name : priya
Age  : 21
DOB  : 11/11/1996
Salary : 3.75l
```

- **To over write the content**

```
Syntax :
cat file1 >file 2

Example :
root@d7e3573d5eb5:/pramati# cat employee>employee1
root@d7e3573d5eb5:/pramati# cat employee1

Output :
name:prasanna
age:21
dob:12/12/1997
Salary:3.75l
position:Assosiate
```

- **To append the content**
```
Syntax:
cat file1>>file2

Example :
root@d7e3573d5eb5:/pramati# cat employee>>employee1
root@d7e3573d5eb5:/pramati# cat employee1

Output:
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
```

- **Moves a file**

```
syntax :
mv filename1 filename2

Example :
root@d7e3573d5eb5:/pramati# mv employee1 company
root@d7e3573d5eb5:/pramati# cd company
root@d7e3573d5eb5:/pramati/company# ls

Output :
employee1  employee_details
```

- ** To copy a file**
```
Syntax:
cp filename1 filename2

Example:
root@d7e3573d5eb5:/pramati/company# cp employee_details employee_personal_details 
root@d7e3573d5eb5:/pramati/company# cat employee_personal_details

Output :
Name : priya
Age  : 21
DOB  : 11/11/1996
Salary : 3.75l
```
-  *To remove a file.**
```
syntax:
rm filename

Example:
root@d7e3573d5eb5:/pramati/company# rm employee_personal_details
root@d7e3573d5eb5:/pramati/company# ls

Output:
employee_details  pramati
```
 
- **Compares files, and shows where they differ**
```
Syntax :
diff filename1 filename2 

Example :
root@d7e3573d5eb5:/pramati/company# diff employee employee_details

Output :
1,4c1,5
< Name  :  prasanna
< Age   : 25
< DOB   :12/12/1993
< Salary: 31k

< Name : priya
< Age  : 21
< DOB  : 11/11/1996
< Salary : 3.75l
```
- **To Tell you how many lines, words, and characters there are in a file**
```
Syntax :
wc filename

Example :
root@d7e3573d5eb5:/pramati/company# wc employee

Output :
 4 10 59 employee
 ```

- **Tells the current date**
```
Syntax :
date

Example : 
root@d7e3573d5eb5:/pramati/company# date

Output :
Thu Jan 24 05:20:26 UTC 2019
```

- **The find command finds all of the files within a directory and its subdirectories that match a set of conditions.**

```
Syntax :
find 

Example :
root@d7e3573d5eb5:/pramati# find company

Output:
company
company/employee
company/employee_details
company/pramati
```
