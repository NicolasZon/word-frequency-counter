# word frequency counter
This is an algorithm that reads a text file and counts the frequency of words in the given text. 
Then it counts words and characters, also constructs a histogram displaying the words and their frequency.


## How to run it?
The only prerequisite is to have installed [python3](https://realpython.com/installing-python/) in your machine.

Open a terminal and run the command 
```python counter.py```
Thats it, now you have the result on the screen.


## Changing the input text
This application will read the ``input`` file by default, 
if you want to test some paragraphs feel free to modify the mentioned file.

If you have other files you can use them too, just set the file names as a parameter, e.g. 
```python counter.py example1.txt example2.txt```.
Be aware to type the correct names and to have the files in the same folder.


## Algorithm Complexity

### time
The provided algorithm works in ``O(log N)`` complexity.
This is because the words are displayed in order according to the number of times they appear.
In order to do that, it is mandatory to sort the data which gives us this complexity.

### space
The algorithm spends ``O(N)`` space in the worse case, this is when all words are unique.
This space is necessary to count the number of occurrences that a word have.
