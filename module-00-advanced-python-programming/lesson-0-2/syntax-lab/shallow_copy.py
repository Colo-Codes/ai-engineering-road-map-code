# A dictionary that contains a list, and a shallow copy of it
lab = {"name": "syntax-lab", "scripts": ["values.py", "strings.py"]}
shallow = lab.copy()
print("lab:", lab)
print(shallow is lab, shallow["scripts"] is lab["scripts"])

# Change a value in the copy, then change the list inside the copy
shallow["name"] = "copy-lab"
shallow["scripts"].append("lists.py")
print("lab:", lab)
print("shallow:", shallow)

# A list whose items are lists, and a shallow copy of it
groups = [["values.py"], ["lists.py"]]
groups_copy = groups.copy()
print("groups:", groups)
print(groups_copy is groups, groups_copy[0] is groups[0])
groups_copy[0].append("strings.py")
print("groups:", groups)
