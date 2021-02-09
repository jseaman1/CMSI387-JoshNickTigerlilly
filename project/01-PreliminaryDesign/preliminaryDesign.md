# Preliminary Design

## 1.1 – Description of modification/addition to Linux

We will be making modifications to the Linux's `test`, `echo`, and `touch` commands. With the combination of all three of these commands, users will have the ability to first, check or `test` if a file exists given a file name, then if a file under that name already exists, a message will be printed to the terminal informing the user of its existence, but if the file doesn't already exist, a new file will be made under the given name. This can be completed with the command `testtouch <filename>`. 

## 1.2 – Rationale as to why this is a good idea, or what the good points of it are:


```
command 
```



## 1.3 – Preliminary list of [possible] Linux modules that will be modified/affected

* `test`: -f 
* `echo`: echo
* `touch`: touch
 

## 1.4 – Preliminary list of any new modules that you will produce [or 'Not Applicable' if there are none]
Not applicable.
