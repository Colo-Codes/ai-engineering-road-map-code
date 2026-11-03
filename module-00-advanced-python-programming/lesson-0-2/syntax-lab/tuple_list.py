# A tuple of two items: a string and a list of two strings
project = ("syntax-lab", ["values.py", "strings.py"])
scripts = project[1]
print("before:", project)

# Change the list inside the tuple
project[1].append("tuples.py")
print("after:", project)
print(project[1] is scripts)
