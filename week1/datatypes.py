#Setting the datatype
x = 5
print(type(x))

x = "Hello world"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(x)

x = range(6)
print(type(x))

x = {"name": "John", "age": 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))


#Setting the specific datatype
x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(x)
print(type(type(x)))

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict(name = "Johnn", age = 36)
print(x)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(x)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))