#! usr/bin/env python
__author__ = 'AJ'
__email__ = 'arenold@ischool'
__python_version__ = '2.7.4'

""" An alternative to parsing the file line by line is python's 
built in csv reader http://docs.python.org/2/library/csv.html

As mentioned, try / except is useful for error handling, but
is not by itself a control structure
More on Errors in Python @ http://docs.python.org/2/tutorial/errors.html """


"""
Variable Scope & Functions
see more @ http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/Q2/scope.html
"""

x = 1

def addOne(y):
    """A basic function"""
    return y + 2

def addTwo(y):
    """A basic function with a global/local naming conflict
    How does python handle this?"""
    x = 1233
    x += 1
    print 'x inside', x
    return y + 4

def addThree(y):
    """A basic function which modifies global x"""
    global x
    x += 1
    print 'x inside', x
    return y + 5

print 'x before', x
y = addOne(1)
print 'y', y
print 'x after', x

print 'x before', x
y = addTwo(1)
print 'y', y
print 'x after', x

print 'x before', x
y = addThree(1)
print 'y', y
print 'x after', x

""" 
Be careful with lists and other objects, here are
three different functions that modify a list!

More on python data structures @ http://docs.python.org/2/tutorial/datastructures.html
"""
array_x = [1,2]

def appendOneItemGlobalRef(item):
    array_x.append(item)

def appendOneItemUsingAppend(item, list_of_items):
    list_of_items.append(item)
    return list_of_items

def appendOneItemToNewList(item, list_of_items):
    ##items = list(list_of_items)
    ##items.append(item)
    ## OR
    items = list_of_items + [item]
    return items


appendOneItemGlobalRef(3)
print 'global array was modified!', array_x, '\n'

new_array_x = appendOneItemUsingAppend(4, array_x)
print 'new array', new_array_x
print 'old array', array_x
print 'wait what??\n'

completely_new_array = appendOneItemToNewList(5, array_x)
print 'completely new array', completely_new_array
print 'old array', array_x
