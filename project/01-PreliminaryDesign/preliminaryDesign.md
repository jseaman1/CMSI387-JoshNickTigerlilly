# Preliminary Design

## 1.1 – Description of modification/addition to Linux

We will be making modifications to the Linux's `touch` command, in collaborative efforts with `test`, and `echo`. With the combination of all three of these commands, users will have the ability to first, check or `test` if a file exists given a file name, then if a file under that name already exists, a message will be printed to the terminal informing the user of its existence. However, if the file doesn't already exist, a new file will be made under the given name. This can be completed with the command `touch <filename> -test`. 

## 1.2 – Rationale as to why this is a good idea, or what the good points of it are:

Oftentimes, we tend to `touch` files that already exist, and fail to receive any indication of success or failure. As human beings, we crave confirmating and verfication that our actions produced the desired result. However, with the current implementation of the `touch` command, there is ambiguity regarding whether or not the file name we provided with `touch` was created then, or had already been created and the only change that the command had was updating the file's access and modification timestamps to the current time. Our new command will solve this problem by providing the user with feedback if the file had already been created without unintentionally updating the file's access timestamps. Our command can be used as follows:

```
touch <filename> -test
```

With this new and improved command, we have now introduced greater ease, usability, and clarity within and surrounding the `touch` command. This new command eliminates uncertainity regarding whether or not a new file was made. 


## 1.3 – Preliminary list of [possible] Linux modules that will be modified/affected

* `touch`: This modification would be added to the `touch` module. Using `-test` after typing the name of the potentially new file will now perform `test <filename>` and `echo "This file already exists"` if the file already exists and `touch <newfile>` if the file does not already exists at the same time.
* `echo`: Although `echo` won't be directly modified, we will be referencing its module information for its purpose in `touch <filename> -test` to provide user feedback in the form of a simple confirmation message.
* `test`: Similarly, although `test` will not be modified, we plan on referencing its module information an documentation in order to check if a file is already in existence before creating it. 
 

## 1.4 – Preliminary list of any new modules that you will produce [or 'Not Applicable' if there are none]
Not applicable.
