#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
word_python = str[:6]
word_object = str[39:66] + str[106:111]
str = word_object + " " + word_python
print(str)
