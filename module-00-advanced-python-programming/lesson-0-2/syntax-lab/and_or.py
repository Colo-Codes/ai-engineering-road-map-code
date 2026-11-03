# and and or give back one of their two values
print("syntax-lab" or "unnamed")
print("" or "unnamed")
print([] and "first item")
print(["values.py"] and "first item")

# Python runs scripts[0] only when the list has items
scripts = ["values.py", "strings.py"]
print(scripts and scripts[0])
scripts = []
print(scripts and scripts[0])
