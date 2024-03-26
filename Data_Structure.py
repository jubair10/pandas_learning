"""
                        Series
Series : It is defined as a one-dimensional array that is capable of storing
various data types.


"""

import pandas as pd


# x = [1, 2, 3, 4, 5, 6]
# x = {1, 2, 3, 4, 5, 6}
# x = (1, 2, 3, 4, 5, 6)
# x = "HELLO"
x = {"name": "John", "age": 30, "city": "New York"}
x = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# x = 90
# a = pd.Series(list(range(x)))

# we can pass any dtype
a = pd.Series(x)
# a = pd.Series(x,index=['a','b','c','d','e','f'],dtype='float',name='DATASETS')

print(a)
print(type(a))

# print(a[0])


s1 = pd.Series(12,index =[1,2,3,4,5,6,7])
s2 = pd.Series(12,index =[1,2,3,4])

print(s1+s2)
'''
1    24.0
2    24.0
3    24.0
4    24.0
5     NaN
6     NaN
7     NaN

Here,
This data represents a series of values where most entries are 24.0, with some missing values denoted by NaN (Not a Number).
'''



















