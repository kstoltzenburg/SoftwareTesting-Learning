Linux
=====

Some basic notes on anything Linux.

## Characteristics


## Basics

### Files

#### File information

Display (list) information on files

```
$ ls -l
-rwxr-xr-- 1 myUser users 2344 Okt 04 14:51 myFile
```

The file myFile has a size of 2344 Bytes, was last changed on Okt 04th 14:51, belongs to the User myUser and to the group users; one hardlink exists for this file.

#### File access rights

Concerning Notation on User rights / file type (-rwxr-xr--):

```
[0]: Filetype, e.g 

     -   regular file
     d   directory
     s   unix-domain-socket
     p   pipe
     b   block-device
     c   character-device
     l   symbolic link
```

```
[1-3,4-6,7-9]: Access rights rwx (read, write, execute) for user, group, other.
```

### File system

Devices in Linux are stored under /dev ; also pseudo-devices without any hardware equivalent;
e.g. /dev/null which serves as a black hole that discards all data you write to it.

```
$ [something] > /dev/null
```
