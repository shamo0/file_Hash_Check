# File Hash Check

SY402 Lab08
Genadi Shamugia, Jackson Stallone

## hash.py

Running hash.py on the command line ("./hash.py" from any directory) will create a file called 
"output.txt". This file contains a hash of every file on the file system, the filename, 
the path to the file, and the data and time in which the hash was taken. 
	
hash.py works by using pythons os.walk library function to step through the file system. 
We used SHA-256 to generate the hash, and datetime library to obtain the date and time the 
hashing took place. 

