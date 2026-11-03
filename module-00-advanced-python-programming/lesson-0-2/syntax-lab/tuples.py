# A tuple of three ints
version = (3, 13, 15)
print(version)
print(type(version), len(version))

# Indexing works as it does for a list
print(version[0], version[-1])

# A tuple with one item needs a comma
in_parentheses = ("main.py")
one_item = ("main.py",)
print(in_parentheses, type(in_parentheses))
print(one_item, type(one_item), len(one_item))

# The empty tuple
print((), len(()))
