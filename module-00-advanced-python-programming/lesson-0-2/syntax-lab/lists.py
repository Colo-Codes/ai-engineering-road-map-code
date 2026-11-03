# A list of three strings
scripts = ["values.py", "strings.py", "main.py"]
print(scripts)
print(type(scripts), len(scripts))

# Indexing
print(scripts[0], scripts[2])
print(scripts[-1], scripts[-3])

# Slicing creates a new list
print(scripts[0:2])
print(scripts[1:])
print(scripts)

# Changing one item
scripts[2] = "string_methods.py"
print(scripts)
