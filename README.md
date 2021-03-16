# MVersion-Control-System

MVCS is a super simple and lightweight version control system written in python that uses no external libraries.

# Installation

To install it simply create a folder then insert your project folder and mvcs.py in it.

# Commands

Here is a list of the commands you can use with MVCS:

#### init

The init command allows you to initialize your repository. It takes one argument that is your project folder name.

```
$ python mvcs.py init MyProject
```

This will create the .mvcs directory which containes all of the repository information.

#### checkout

The checkout command allows you to switch or create branches, by default you will have a master branch. It takes one argument that is the name of the branch: if it exists, it will switch you to that branch, if not it will create it and then switch to it.

```
$ python mvcs.py checkout MyBranch
```

#### commit

The commit command allows you to save the state of your project in the branch you're currently working in. It takes one argument that is the message of the commit.

```
$ python mvcs.py commit "My first commit!"
```

#### revert

The revert command allows you to go back to a previous state of your project. It takes one argument that is the commit number of the branch you're currently working in that you want to revert to.

```
$ python mvcs.py revert 1
```

#### log

The log command allows you to get information about your repository. If no argument is specified it will log all of your branches and the number of times you committed to them, if a branch is specified it will log all of the commits you made to that branch and their respective messages.

```
$ python mvcs.py log master
```
