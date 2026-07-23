## LEARN DATA STRUCTURES AND ALGORITHMS WITH ME!

im finally tackling this knowledge and im excited to share my approach with you guys. 

i finally have a foothold on a prespective thats given me some momentum so work with me as i formalize it. hope it will help some others too

# Lesson 1: every problem can use its own data structure depeneding on the access pattern you need
every time you hear a problem, figure out what the best data structure is for it

- problem = what the data is (how its related) and how you're accessing it (how do you use it)

examples: 
- some unique ID with related data -> DICT/HASH
- data that's sequential -> LIST 

# Lesson 2: be conscious of the data you need to RETURN 
you may be working with data that makes sense to have in a list. but if you need to reference the unique ID for that data, you'll need both representations (the dict and the list) 
- this is so you can efficiently work with the data and maintain the key/value relationship 

# Lesson 3: stateless vs stateful 
this made me think about what this term really is and it makes sense now. 

for the in-memory class, the data being fed to this system is stored in the linux process running the application
if you have multiple instances of the app running behind a load balancer, you cannot hit an arbitrary process if you're now trying to fetch that data. it must hit the process that handled the write request because the data is sitting in its memory. 
if your data lives somewhere centralized (like a DB), the application and all its instances can now read/write to this place. now the app is stateless.


# classes 
- useful for having multiple instances of the same thing(?)
- if you declare list [] at top of file, you're sharing data for different implementations
- a class gives you as many lists [] and all associated data structures + methods in isolation 

# good little tidbits 
- the tiebreak is the second element when sorting tuples in python 
    - you can add a second data point to tiebreak on, but this makes the tuple 1 element bigger (data_1, tiebreak, data_2)
