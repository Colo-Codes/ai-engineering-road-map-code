# Tuples as set members
versions = {(3, 13), (3, 12), (3, 13)}
print(versions, len(versions))

# Ints and tuples as dictionary keys
reasons = {200: "OK", 404: "Not Found"}
print(reasons[404])
released = {(3, 13): 2024, (3, 12): 2023}
print(released[(3, 13)])

# A list as a set member
# groups = {["values.py", "strings.py"]}
groups = {("values.py", "strings.py")}
print(groups)
