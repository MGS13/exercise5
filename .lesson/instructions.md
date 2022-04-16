# Exercise 05: Implementing Autosave and Autoload
We take autosave and autoload for granted in video games. I'm old enough to remember a time when you had to *manually* save your game every few minutes, like an animal. Yuck. Anyway, the NEA project usually wants you to be able to save the data to a file - and that's all fine and dandy but the minute you start creating your own file structure is the moment when your project gets out of your hands and becomes a nightmare of Lovecraftian proportions.

Why don't we steal the autosave and autoload ideas from the best videogames and use those instead?

## Getting Started
To start with we're going to take a look at a program that stores the prices of phone sales. It uses a lot of the techniques we've used so far, but the basic gist of it is that a user can press 1 to add a new sale, which gets put in a 2D array, or press 2 to view the sales, which uses a pretty printing function to show the list on the screen in a nice way. It even calculates prices!

```python
import time, os

phoneSales = []

def addSale():
  item = input("Item: ")
  price = float(input("Price: "))
  quantity = int(input("Quantity: "))
  total = round(price*quantity,2)

  row = [item, price, quantity, total]
  phoneSales.append(row)

  print("Added successfully")
  time.sleep(1)

def viewSales():
  print("SALES HISTORY")
  for row in phoneSales:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(1)

while(True):
  print("PHONE SALES")
  print("===========")
  print("Press 1 to add new Sale")
  print("Press 2 to view Sales")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addSale()
  elif(menuChoice=="2"):
    viewSales()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('clear')

```

So when the program is run you'll see this menu.

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 
```

If you decide to add a new sale you can press `1` and get stuck straight into that. Again, please notice is no validation for readability's sake. Here we've added a sale of three iPhone 12s at £989.99 per phone.

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 1
Item: iPhone 12
Price: 989.99
Quantity: 3
Added successfully
```

Once added we are sent back to the menu, and this time if we select to view the sales we see the three iPhones having been stored in the 2D `list` with a total price of £2969.97. Nice.

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 2
SALES HISTORY
iPhone 12   989.99  3   2969.97
```

What happens though if we stop the program and start it up again? Well if we click the stop button, then the run button again and try going straight into viewing the sales we see that absolutely nothing is stored.

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 2
SALES HISTORY
```

**WHY?!** We've just spent ages typing in the details for the sale of three iPhones, *three*!

Unfortunately when we create any variable in a program it *only* gets stored in RAM, when a program is stopped all the data that it created disappears even if it is opened again. That's a major downer, especially if you're spending hours entering test data during the controlled time for your NEA!

## Building Autosave

What we need to do is to get that 2D `list` automatically saved to a file. If you've done file I/O before in Python you'll remember that conceptually it's quite simple - it's just three steps: open the file, change the file, save the file. To get autosave working we'll have to try and do that each time the `list` is changed, and it seems like a good place to do that would be at the bottom of the menu loop. Let's take a look down there.

```python
  …
  os.system('clear')

  f = open("sales.txt", "w")
  f.write(str(phoneSales))
  f.close()
```

You'll see here we've added the code *inside* the `while` loop for the menu, but as the exact last thing the menu does before iterating again, that means it's even after the code to clear the screen.

That first line opens up a file called `sales.txt` in `write` mode, you'll see that from the `"w"` in the argument on `f = open("sales.txt", "w")`, the `"w"` means that the first thing it does is delete any file called `sales.txt` that's already in the same folder. This might seem needlessly destructive but it's the simplest way to do it, and is what your games console does - that's why you get that graphic that says "Saving, do not turn off console" when it does an autosave.

The second line is all we need to make the changes, what we're doing here is putting the `list` directly in the file, of course as we can't write a `list` to a file we have to cast it as a `str` beforehand, but that line `f.write(str(phoneSales))` just puts the array in the new blank file.

Finally we need to save the file to the disk, and this is done with the very simple `f.close()`, don't forget that without this the file **does not save** to the disk and so all you work will have been useless!

When the program is run this time, and a phone is added using option 1, as soon as the menu restarts the file `sales.txt` will appear in the Files window. Opening that up to see what's inside will give us:

### sales.txt
```
[['iPhone 12', 989.99, 3, 2969.97]]
```

Which is *actual code* for the 2D `list` that we generated.

If we were to stop the program now, run it again and press 2 to see the sales history then we'd see…

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 2
SALES HISTORY
```

… aww, sweet naff all really. And that's because we haven't built the autoload function yet.

## Building Autoload
If we want to get the program to open the text file, extract the 2D `list` and load it back into memory when the program starts then the best place for the code to go would be back at the top, immediately under the original definition for the blank `list`. Make a bit of room and add this:

```python
…
phoneSales = []

try:
  f = open("sales.txt", "r")
  phoneSales = eval(f.readline())
  f.close()
except:
  pass

…
```

So there's a lot going on here, let's try and break it down. We are using a similar three-part structure to the code as we've seen for loading before: open the file, read the contents, close the file. The structure means that we can do the load with just one little cheat.

The line `f = open("sales.txt", "r")` is broadly similar to our opening code from before, but this time it's opening the file in `r` mode - read mode - this will allow us to see, but not change, the contents of the file.

We've got a really nice, clever line here for the second part, we'll start with `f.readline()` which just reads the first line from the file as a string. The clever part comes from the `eval` function, as eval will inspect a string, assume it's code and try and execute it - as we've given it the code version of a `list` then `eval` has converted the text version of the list into an actual `list` that can be understood by the computer. The `phoneSales =` part just replaces the original, blank `list` with this new one that's been built from the saved data.

I know you're impressed. The `eval` function is a beautiful cheat that makes it possible to build this autoload function, but **be warned**, you should *never* use the eval function in this way in normal software development because you are executing code that someone else has typed in - an end user, no less - leaving yourself vulnerable to all sorts of nasty script injection attacks. Please only ever use this for an NEA project, or at least research `input sanitisation` to find out what you can do before sending the input to `eval`.

Many people forget about the third part, closing the open file is just as important here. If you forget `f.close()` then there aren't going to be any saving problems, but you do have this file open in read mode and when the code gets to autosave function then the `f = open()` bit just won't work.

There's still more! You'll see the `try` and `except` constructs here, all they are doing are stopping the program crashing if the computer can't find the `sales.txt` file for some reason. `try` essentially says "give this code a go", and the `except` part says "and do this instead of crashing", you'll see we've just used our sneaky `pass` placeholder for that, because if the load attempt does crash then it doesn't really matter - we've created a blank `list` already so let's just carry on with our lives.

Phew! Anyway, now if you run the program it loads the information from the text file and therefore our view sales option gives us this output:

```
PHONE SALES
===========
Press 1 to add new Sale
Press 2 to view Sales
> 2
SALES HISTORY
iPhone 12   989.99  3   2969.97
```

Smashing! That's it really for this section, but it takes practice to get each set of three lines of codes in your head and repeatable. The full working code is below for you to try out yourself.

```python
import time, os

phoneSales = []

try:
  f = open("sales.txt", "r")
  phoneSales = eval(f.readline())
  f.close()
except:
  pass

def addSale():
  item = input("Item: ")
  price = float(input("Price: "))
  quantity = int(input("Quantity: "))
  total = round(price*quantity,2)

  row = [item, price, quantity, total]
  phoneSales.append(row)

  print("Added successfully")
  time.sleep(1)

def viewSales():
  print("SALES HISTORY")
  for row in phoneSales:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(1)

while(True):
  print("PHONE SALES")
  print("===========")
  print("Press 1 to add new Sale")
  print("Press 2 to view Sales")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addSale()
  elif(menuChoice=="2"):
    viewSales()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('clear')

  f = open("sales.txt", "w")
  f.write(str(phoneSales))
  f.close()
```

## Your Task
You have been given a basic version of a video game rentals program (*It's like I've been looking back through the old code or something!*), extend this program so that it:

1. Uses a 2D `list` to store the data
2. Uses autosave to store the data in a file called `gameRentals.txt`
3. Use autoload to load the 2D `list` from the `gameRentals.txt` file on each load
4. You'll see that the program also contains a `list` of customers in a file called `customers.txt`, write some autoload code to create a list called `customers` that loads this data
5. Extend the program to be able to create customers
6. Write an autosave function to be able to save the customers list back to `customers.txt`, you should not delete any existing customers whilst doing this

### Extension

5. Go back through any of your other exercise files that used 2D `lists` and add in code to use autosave and autoload, making sure that the file names you are using to store you data in are sensible

  