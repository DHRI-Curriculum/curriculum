## Creating files and folders

### Creating a folder

So far, we've only performed commands that give us information. Let's use a command that actually affects the computer. 

First, make sure you're in the home directory:

```
$ pwd
/Users/patrick
```

Let's move to the Desktop folder with `cd`:

```
cd Desktop
```

Once you've made sure you're in the Desktop folder with `pwd`, let's try a new command:

```
touch foo.txt
```

If the command succeeds, you won't see any output. Now move the terminal window and look at your "real" desktop, the graphical one. See any differences? If the command was successful and you were in the right place, you should see an empty text file called "foo.txt" on the desktop. Pretty cool, right?

### Creating folders

OK, so we're going to be doing a lot of work during the Digital Research Institute. Let's create a project folder in our home directory so that we can keep all our work in one place.

First, let's check to make sure we're still in the Desktop folder with `pwd`:

```
$ pwd
/Users/patrick/Desktop
```

Once you've double-checked you're in Desktop, we'll use this command to make a folder called "projects":

```
mkdir projects
```

Now do `ls` to see if a projects folder has appeared. Once you confirm that the projects folder was created successfully, `cd` into it. 

```
$ cd projects
$ pwd
/Users/patrick/Desktop/projects
```

OK, now you've got a projects folder that you can use throughout the Institute. It should be visible on your graphical desktop, just like the `foo.txt` file we created earlier. 

### Example

![Creating files and folders](make-file-folder.gif)
