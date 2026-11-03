# Adding items
scripts = ["values.py", "strings.py"]
scripts.append("main.py")
print(scripts)
scripts.insert(1, "quote_error.py")
print(scripts)

# Keep the item removed by .pop()
last = scripts.pop()
print("popped:", last)
print(scripts)
first = scripts.pop(0)
print("popped:", first)
print(scripts)

# .remove() finds a value, del uses an index
scripts.remove("strings.py")
print(scripts)
del scripts[0]
print(scripts, len(scripts))

# Sorting
scripts = ["values.py", "strings.py", "main.py"]
in_order = sorted(scripts)
print("sorted:", in_order)
print("scripts:", scripts)
result = scripts.sort()
print("scripts:", scripts)
print("result:", result)
