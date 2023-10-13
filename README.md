<div align="center">
<h3>AirBnB clone - The console</h3>
  <img src="airbnb.webp" width="500" height="350"/>
</div>

### **Welcome to the AirBnB clone project!**
The Minishell console project is designed to create a shell application that operates in both interactive and non-interactive modes. This project serves as a fundamental emulation of Airbnb's console, offering basic functionalities similar to Airbnb's operations.

## **The console**
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to build later, there won’t be a need to pay attention (take care) of how the objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
# Getting Started

These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

## Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
```
git clone https://github.com/MahderZergaw/AirBnB_clone.git
Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
##### Authors: **`Mahder Zergaw`** & **`Oluwatosin Ajayi`**

