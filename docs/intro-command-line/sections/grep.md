### Searching text data

So we've cleaned our data set, but how do we find entries that use a particular term? 

Let's say I want to find all the entries in our data set that use the term "Paris."

```
$ cat nypl_items.csv | grep -i "paris"
[...]
```

This will print out all the lines that contain the word "Paris." (The `-i` flag makes the command ignore capitalization.) Let's use our `wc -l` command to see how many lines that is:

```
$ $ cat nypl_items.csv | grep -i "paris" | wc -l
191
```

### Challenge

Use the `grep` command to explore our .csv file a bit. What areas are best covered by the data set?

### Before we finish...

Before you leave today, let's prepare for the next session by organizing your projects folder on your desktop. First, in your projects folder, create a new folder for each of our workshops and one for our cheat sheet:

```
$ pwd
/Users/patrick/Desktop/projects
$ mkdir git
$ mkdir python
$ mkdir databases
$ mkdir cheatsheet
```

Then move your `cheat-sheet.txt` file into your `git` folder and your `nypl_items.csv` into your `databases` folder with the `mv` command:

```
$ mv cheat-sheet.txt git
$ mv nypl_items.csv databases
```

### What next?

That's the end of the command line session, but if you want to continue to learn about the command line, take a look at the [other useful commands](other-commands.md) or [additional challenges](challenges.md).

[Go to other commands >>>](other-commands.md)  
[Go to further challenges >>>](challenges.md)  

### Example

![Searching a text file with grep](grep.gif)



