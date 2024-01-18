# Clean Cracker
Clean Cracker is a tool for creating rainbow tables, cracking passwords and performing password-security audits. 


How to use (Lam finishd):

Create Rainbow:
workspace/demo_files/10k_most_common_passwords.csv

Cracking:
workspace/password_lists/rainbow_small.csv
workspace/demo_files/password_database_dump.csv
sha256

---

## User Interaction
The user can interact with Clean Cracker classical via the system console or via a simple graphical user interface. 

The input and output files are always required and provided in .csv format. 

The output files are provided in workspace/output. 

Input files are provided in:
- workspace/password_raw_files: for list of most common passwords
- workspace/rainbow_files: for rainbow tables
- workspace/target_files: for password hash lists to crack

Users can either use own rainbow tables or most common password lists or use the predefined versions in the respective folders. 

---

## Functionalities
### Create your own rainbow tables
Passwords are not stored in plaintext but as hashes in databases. 
The process of hashing large amounts of data is computationally intensive, 
therefore tables with plaintext passwords and the hashes versions of the passwords are prepared. 
A rainbow table is a table with plaintext passwords and one or more hashes of the password. 

Clean Cracker allows users to use own plaintext password lists and generate a rainbow table. 
The tool supports several hash algorithms (see below). 
The generated rainbow tables can consist of some or all of the hash types. 

### Crack password lists
Clean Cracker offers a functionality to crack hashed password lists e.g., database dumps. 
The cracking is done by comparing the targeted password hashes with a rainbow table. 
From the intersection set of rainbow table hashes and target password list hashes the 
plaintext passwords are obtained in the rainbow table and entered to the original target file. 

### Password auditing / find weak passwords
Weak passwords are a major security risks. 
Clean Cracker offers a functionality for system administrators to test the strength of 
user passwords without cracking them. 
Therefore, a password list e.g., from a database is entered with a list of most common passwords. 
The tool calculates the hashes of the most common password list and compares it with the user password hashes. 
Users with passwords found in the most common password set are market in the original file. 

### Brute forcing
Brute forcing is an alternative to rainbow tables and involved trying out all possible strings of letters and numbers 
to find the password. 
Clean Cracker offers a brute force cracking functionality for passwords. 

---

CURRENT_SUPPORTED_ALGORITHMS: 
"md5", "sha1", "sha224", "sha256", "sha384", "sha512"

---
