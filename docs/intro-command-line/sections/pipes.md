## Pipes

So far, you've learned a number of commands and one special symbol, the `>` or redirect. Now we're going to learn another, the `|` or "pipe."

Pipes let you take the output of one command and use it as the input for another.

Let's start with a simple example:

```
$ echo "Hello from the command line" | rev
enil dnammoc eht morf olleH
```

In this example, we take the output of the `echo` command ("Hello from the command line") and pipe it to the `rev` or reverse command. The result is the reverse of the text that we entered.

Let's try a more practical example. What if we wanted to put the commands in our cheat sheet in alphabetical order?

Use `pwd` and `cd` to make sure you're in the folder with your cheat sheet. Then try:

```
cat cheat-sheet.txt | sort
```

You should see the contents of the cheat sheet file with each line rearranged in alphabetical order. If you wanted to save this output, you could use a `>` to print the output to a file, like this:

```
cat cheat-sheet.txt | sort > new-cheat-sheet.txt
```

### Example

![Pipes example](pipes.gif)
