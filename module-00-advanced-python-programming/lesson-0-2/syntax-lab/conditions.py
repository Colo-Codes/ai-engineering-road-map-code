# if: a block that runs only when the condition is True
status_code = 404
if status_code == 200:
    print("The request succeeded")
if status_code >= 400:
    print("The request failed")
    print("Status code:", status_code)
print("Both if statements are finished")

# if and else: exactly one of two blocks runs
scripts = ["values.py", "strings.py", "main.py"]
if "lists.py" in scripts:
    print("lists.py is in the list")
else:
    print("lists.py is missing")

# if, elif and else: the first True condition wins
name = "syntax-lab"
if len(name) > 20:
    print(name, "is a long name")
elif len(name) > 5:
    print(name, "is a medium name")
else:
    print(name, "is a short name")

# Separate if statements: Python checks every condition
if len(name) > 5:
    print("more than 5 characters")
if len(name) > 8:
    print("more than 8 characters")
