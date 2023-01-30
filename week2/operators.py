#Python Operators
print(10 + 5)

#Python Arithmetic Operators
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)

x = 12
y = 3
print(x / y)

x = 5
y = 2
print(x % y)

x = 15
y = 2
print(x ** y) #same as 2*2*2*2*2

x = 2
y = 5
print(x // y) #the floor division // rounds the result down to the nearest whole number

#Python Assignment Operators
x = 5
print(5)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x >>= 3
print(x)

x = 5
x << 3
print(x)

#Python Comparison Operators
x = 5
y = 3
print(x == y)

print(x != y)

print(x > y)

print(x < y)

print(x >= 3)

print(x <= y)

#Python Logical Operators
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

#Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)   # returns True because z is the same object as x
print(x is y)   # returns False because x is not the same object as y, even if they have the same content
print(x == y)   # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)   # returns False because z is the same object as x
print(x is not y)   # returns True because x is not the same object as y, even if they have the same content
print( x != y)      # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Python Bitwise Operators
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(x | y)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================
"""

print(x ^ y)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""

print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(3 >> 2)
"""
The >> operator moves each bit the specified number times to the right. Empty holes at the left is filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""