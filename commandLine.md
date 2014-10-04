# Personal notes on command line tools & examples

List information on files

    $ ls -l
    -rwxr-x-r-- 1 myUser users 2344 Okt 04 14:51 myFile

The file myFile has a size fo 2344 Bytes, was last changed on Okt 04th 14:51, belongs to the User myUser and to the group users; one hardlink exists for this file.

> Concerning Notation on User rights / file type (-rwxr-x-r--):

[0]: Filetype, e.g - (regular file), d (directory), s (unix-domain-socket), p (pipe), b (block-device), c (character-device), l (symbolic link)

[1-2,3-5,6-8]: Access rights rwx (read, write, execute) for user, group, other.

--

Devices in Linux are stored under /dev ; also pseudo-devices without any hardware equivalent;
e.g. /dev/null which serves as a black hole that discards all data you write to it.

    $ [something] > /dev/null

