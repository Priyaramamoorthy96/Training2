# Unix
## Install ubuntu in docker

Run the following to get the ubuntu to be insatalled
 
 - docker run -it ubuntu bash

## Unix commands

- ls --- lists your files.

- ls -l --- lists your files in 'long format'.

- ls -a --- lists all files, including the ones whose filenames begin in a dot, which you do not always want to see. 

- mkdir dirname --- make a new directory

- cd dirname --- change directory.

- pwd --- tells you where you path
- vi
 
    - 1.To use vi in ubuntu docker 

        - docker exec -it containername  bash
        

    - 2.then run the following commands

       - apt-get update

      - apt-get install vim

- cat - to show the content of the file

- cat file1 >file 2 - over write the content

- cat file1>>file2 - append he content

- mv filename1 filename2 --- moves a file 

- cp filename1 filename2 --- copies a file

- rm filename --- removes a file.
 
- diff filename1 filename2 --- compares files, and shows where they differ

- wc filename --- tells you how many lines, words, and characters there are in a file

- date - tells the current date

- find - The find command lists all of the files within a directory and its subdirectories that match a set of conditions. 
