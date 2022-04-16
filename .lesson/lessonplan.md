# Exercise 05: Autosave and Autoload

## Learning Objectives
1. Students will understand the three part structure to a manual load or save procedure
2. Students will be able to apply the standard file save methodology to saving their 2D data structure at the end of each menu iteration
3. Students will be able to apple the standard file load methodology to restoring their 2D data structure from files
4. Students will be able to use `eval` to convert text output back into working code, and be aware of the security implications of using this method in production code
5. Students will have experience using the `try` and `except` constructs to avoid program ending crashes when using file I/O
 
## Overview
This unit should take around one hour to complete, however the extension may run the work into the two hour region. 

The autosave and autoload routines here have been designed to be short, memorable and repeatable in controlled conditions. Please push the idea with your students that if, after all the work to set up the 2D list they than have to completely design a file structure for saving then they'll be doubling down on the work they need to do in a finite amount of time. These are repeatable and importantly mean that if they implement them quickly enough all of their test data will be usable during the development process.

In most NEA scenarios the ability to load the data from the file is not explicitly requested, so if students are running out of time the autosave code is often enough to get them through to a 'complete' project, but the addition of the autoload really will speed up their development time in not having to completely reenter every piece of data they need each time they want to test their code.

Students will often stumble with exactly where they need to build each aspect of the code, so the extension activity is very powerful for reinforcing that idea without getting them to build an entire working program from scratch. After two or three attempts most students will understand where to locate these features for the win.

## Delivering the content in class

1. ***Getting Started*** (10 minutes) Copy the code for the basic program and run through the process of adding an item of data, showing it with the printing function then terminate and reload the program. Get the students to discuss why the data doesn't load, what's the different between Primary and Secondary and storage and how we can access that secondary storage.for persistent data storage needs. If students have worked on file I/O problems before get them to talk about the issues they faced and how fiddly and inconsistent the experience can be.

2. ***Building Autosave*** (15 minutes) Model the autosave code and pay particular attention to the `str` casting inside `f.write()` as this is an often forgotten part. Show the students the sales.txt file before and after the addition of data through the program. Show the program loading from a suspended state and explain why nothing is yet loading. Ask the students to implement this stage of the build.

3. ***Building Autoload*** (15 minutes)  Model the build of the autosave code. Explain in *laborious* detail the `eval` function, how it converts text to working code and be at plains to express that this *should not be used in production code* because of the ridiculous amount of issues with running user entered data as code. Injection attacks are then worth discussing, particularly SQL injection attacks as a common vulnerability in online platforms. Student are unlikely to have come across `try` and `except` before, ensure that they develop an understanding of the constructs use here to attempt code but run alternative code if the `try` crashes. Again, ask them never to use the `pass` on the `except` clause in production code, it should always be reporting errors clearly, but for our purposes here this is not necessary as the blank `list` is used if nothing can be loaded. Give students to opportunity to build the load commands.

4. ***Task*** (20 minutes - extension may take up to an hour longer) The build of the task itself should be reasonably straightforward however they may struggle with the multiple 2D `list` storage - in reality this is just running the code twice. Some may be tempted to use on `try` `except` construct to load both, tell them *never* attempt two loads in one `try` as if either of them fails it terminates the code so you really need them separately.


  