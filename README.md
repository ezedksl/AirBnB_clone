<p align="center">
  <img width="384" height="162" src="https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67">
</p>

---
# <span style="color:#dd4646">**AirBnB clone**</span>
* This project is the first part of a clone of the AirBnB web.
* This includes a console that creates, destroys, updates and shows instances of different elements.
---
### <span style="color:#dd4646">**Getting Started:**</span>
---
* Clone this repo.
* Open terminal from cloned folder path.

**To execute the program, you can either execute it in the interactive mode:**

>Typing `./console.py` from the terminal:

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
**And also in the non-interacvtive mode:**
>(example) `echo "help" | ./console.py`:
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
---
### <span style="color:#dd4646">**List of commands:**</span>
---
>`help`:
  * Shows a list of commands. In case of writing `help <command>` it will print a description of the command

>`create`:
  * Creates a new element.
  * Usage: `create <class_name>`. Also prints the id of the element created.

>`show`:
  * Prints the string representation of an element.
  * Usage: `show <class_name> <element_id>`

>`destroy`
  * Deletes an element.
  * Usage: `destroy <class_name> <element_id>`

>`all`:
  * Prints string representation of all elements, or in case of adding the class name it will print all elements based on it
  * Usage: `all` or `all <class_name>`

>`update`: Updates or adds attributes to the given element.
  * Usage: `update <class_name> <element_id> <attribute_name> "<attribute_value>"`
 ---
>`quit`:
  * Exits the console

>`EOF`/`Ctrl+D`:
  * Exits the console

---
### <span style="color:#dd4646">**Examples**:</span>
---
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

```
(hbnb) create BaseModel
b0a79339-8b0c-4827-9c46-04a051cbd5c5
```

```
(hbnb) show BaseModel b0a79339-8b0c-4827-9c46-04a051cbd5c5
[BaseModel] (b0a79339-8b0c-4827-9c46-04a051cbd5c5) {'id': 'b0a79339-8b0c-4827-9c46-04a051cbd5c5', 'created_at': datetime.datetime(2021, 2, 18, 20, 44, 45, 659192), 'updated_at': datetime.datetime(2021, 2, 18, 20, 44, 45, 668831)}
```

```
(hbnb) all BaseModel
["[BaseModel] (1ab45d5f-5c1e-4799-9f5e-b39047e45875) {'id': '1ab45d5f-5c1e-4799-9f5e-b39047e45875', 'created_at': datetime.datetime(2021, 2, 18, 20, 46, 56, 17896), 'updated_at': datetime.datetime(2021, 2, 18, 20, 46, 56, 18565)}", "[BaseModel] (45aefd37-695f-428e-adaa-1e046d87d192) {'id': '45aefd37-695f-428e-adaa-1e046d87d192', 'created_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 157250), 'updated_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 158015)}"]
```

```
(hbnb) destroy BaseModel 1ab45d5f-5c1e-4799-9f5e-b39047e45875
(hbnb) all
["[BaseModel] (45aefd37-695f-428e-adaa-1e046d87d192) {'id': '45aefd37-695f-428e-adaa-1e046d87d192', 'created_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 157250), 'updated_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 158015)}"]
```

```
(hbnb) update BaseModel 45aefd37-695f-428e-adaa-1e046d87d192 name "Pepocho"
(hbnb) all
["[BaseModel] (45aefd37-695f-428e-adaa-1e046d87d192) {'id': '45aefd37-695f-428e-adaa-1e046d87d192', 'created_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 157250), 'updated_at': datetime.datetime(2021, 2, 18, 20, 47, 2, 158015), 'name': 'Pepocho'}"]
```

---
### <span style="color:#dd4646">**Testing**:</span>
---
There are some test in the repo that can be ran with the following command:
>`python3 -m unittest discover tests`
```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 198 tests in 2.342s

OK
guillaume@ubuntu:~/AirBnB$
```
---
### <span style="color:#dd4646">**Authors**:</span>
---
* Ezequiel Martinez
* Hugo Gomez
