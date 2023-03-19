# Password-Manager

This is a simple password manager coded in Python to store all your passwords locally. 
It is encrypted with a key of your choice.
It is highly efficient, light and has a stunning design. 
It uses binary files to store the data and keys. 


INSTRUCTIONS:

In order to start using the application you must first create a new databse binary file and a key. This is done using the pickle module and manually creating the binary file. Moreover you need add new passwords initially to use the password manager. But you can also use the sample.dat file in the repository to test the application if required.

-> Creating a new .dat file:
   1. Go to the application folder and create new <file_name>.dat file
   2. In the code under files and keys, replace 'sample.dat' with <file_name>.dat

-> Create a new key:
   1. This part requires the use of the pickle module in python.
   2. Create a <key_file>.dat file.
   3. Use the pickle.dump("your_key",<key_file>) function
   4. Replace 'your_key.dat' with <key_file>.dat in the main function
   
   
