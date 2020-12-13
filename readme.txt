
NOV 2020 
Hello! Welcome to Cryptext, a barebones text editor that automatically encrypts on save.
Here is what is left to be done in Cryptext:
1. Create the "Save and Encrypt Function"
   - this function should save the file, and, before saving, run the file through the
     twofish encryption algorithm (not dead set on this algorithm but after researching
     it appears this algorithm is commonly used for encrypting files).
2. Create the "Save As and Encrypt" function
    - this function, like the "save and encrypt" function, allows the user to define the
    name and save location of the file, as well as encrypting it. I am intending for this
    to be a recursive function that will call "save and encrypt" and pass the user's
    specified filename and save location
3. Create the "open file" function
    -This function has two parts: the first will present a dialogue box for the user to enter
    the password for the file. After the correct password is entered, the file will be opened
    for the user to either read or edit. The second part is that this function will have a
    password failsafe that, after several attempts (number undecided), will wipe completely
    delete the file from the user's computer for security reasons.

Author's note: while the idea for this software is my own, I did follow a YouTube tutorial which can be found here (https://www.youtube.com/watch?v=7PGFin30c4o) to implement some of the basic functions of a text editor using Tkinter. I did not use all of the code described in this video, but I did use parts of it :)
