# A set from a list: each value appears once
codes = [404, 200, 404, 500, 200]
unique_codes = set(codes)
print(codes, len(codes))
print(unique_codes, len(unique_codes))
print(type(unique_codes))

# A set written with curly braces
scripts = {"values.py", "strings.py", "main.py", "strings.py"}
print(len(scripts))
print(sorted(scripts))

# in checks whether a value is a member
print(404 in unique_codes, 301 in unique_codes)
print("main.py" in scripts)

# An empty dictionary and an empty set
print(type({}), type(set()))
print(set(), len(set()))
