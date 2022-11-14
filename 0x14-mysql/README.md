# Files and their finctions
- 4-mysql_configuration_primary, 4-mysql_configuration_replica - Setup a Primary-Replica infrastructure using MySQL
- 5-mysql_backup - Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
  - Requirements:
    - The MySQL dump must contain all your MySQL databases
    - The MySQL dump must be named backup.sql
    - The MySQL dump file has to be compressed to a tar.gz archive
    - This archive must have the following name format: day-month-year.tar.gz
    - The user to connect to the MySQL database must be root
    - The Bash script accepts one argument that is the password used to connect to the MySQL database
