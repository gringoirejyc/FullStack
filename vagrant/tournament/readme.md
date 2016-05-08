# Tournament Result using PSQL & Python
This project is a part of Udacity **Full Stack Web Developer** Nanodegree project.
Using [swisspairing system](https://en.wikipedia.org/wiki/Swiss-system_tournament) to pair the matches. 
This project is to develop a database schema to store the game matches between players. Using Python module to rank the players and pair them up in matches in a tournament.
Three file include, one is SQL file, one is funcation file, one is test file

##Quick Start
This project require [Vagrant](https://www.vagrantup.com/) & [Virtual Box](https://www.virtualbox.org/)

###Install
1. Fork this respository to your local computer
2. Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine. In your terminal ,type `cd Users/YourPcName/Deskstop/FullStack/vagrant/tournament` & `vagrant up`

3. Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt.  To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it. Type `vagrant ssh` to **log in**. If you want to **turn off** the vagrant ,type `vagrant halt`
4. Make sure your directory is the project folder, then to import the databse & table, in your terminal type `psql -f tournament.sql`
5. To test the code, in your terminal type `python tournament_test.py`
6. To see the data in the database, type `psql`, then type some SQL queries.


Files installed for this project are located in the /vagrant directory inside the virtual machine. Everything here is automatically shared with the vagrant directory inside the fullstack directory on your computer. Any code files you save into that directory from your favorite text editor will be automatically available in the VM.

If you’d like to see what was installed in the VM, look in /vagrant/pg_config.sh.

In this project you will mostly be running your work in Python from the command line. In addition you’ll use the psql program to interact with the PostgreSQL database.

To connect psql to the forum database for Lesson 3, type psql forum at the command line. To exit psql, type \q or Control-D (^D).



###Issues
In the player table, the player id start from 9 for the first time use, it suppose to start from 0

###Licence
This is a public domain work, dedicated using CC0 1.0. Feel free to do whatever you want with it.
