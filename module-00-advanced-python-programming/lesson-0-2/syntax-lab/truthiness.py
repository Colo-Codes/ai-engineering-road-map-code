# Falsy values: bool() gives False for each one
print(bool(False), bool(None), bool(0), bool(0.0))
print(bool(""), bool([]), bool(()), bool({}), bool(set()))

# Truthy values: bool() gives True for each one
print(bool(404), bool(-1), bool(0.5))
print(bool("0"), bool(" "), bool([0]), bool({"timeout": 0}))

# A list as the condition of an if statement
scripts = ["values.py", "strings.py"]
if scripts:
    print("scripts has", len(scripts), "items")
else:
    print("scripts is empty")

scripts = []
if scripts:
    print("scripts has", len(scripts), "items")
else:
    print("scripts is empty")

# not turns a value into the opposite bool
print(not scripts, not "syntax-lab")
