"""The Namedtuple() solves a very major problem in the field of computer science.
Usual tuples need to remember the index of each field of a tuple object, however,
namedtuple() solves this by simply returning with names for each position in the tuple.

In the following code, an index is not required to print the name of a student rather
passing an attribute is sufficient for the required output."""

from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('Peter', 'James', '13')
print(s1.fname)