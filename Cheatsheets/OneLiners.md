Command line one-liners
====

A collection of command line one-liners.

## Sources
* https://arturoherrero.com/command-line-one-liners/
* https://github.com/arturoherrero/command-line-one-liners
* https://twitter.com/climagic
* https://twitter.com/UnixToolTip



## One Liners

### List the 20 largest files or folders under the current working directory

```
$ du -ma | sort -nr | head -n 20
```

Less accurate (rounding), but more human readable:

```
$ du -ha | sort -rh | head -n 20
```

### Return number of lines, words and bytes in a file

```
$ wc
```

Use -l, -w, -c to get just one of these.



