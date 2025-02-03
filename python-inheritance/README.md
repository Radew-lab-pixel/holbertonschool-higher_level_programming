### Week 16 : Python : Inheritance

### Task 0 : Write a function that returns the list of available attributes and methods of an object:

0-lookup.py
#!/bin/usr/python3

def lookup(obj):
    return dir(obj)

0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass
print(lookup(MyClass1))
print(lookup(MyClass2))
