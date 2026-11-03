import copy

# A dictionary that contains a list, and a deep copy of it
lab = {"name": "syntax-lab", "scripts": ["values.py", "strings.py"]}
deep = copy.deepcopy(lab)
print(deep == lab, deep is lab, deep["scripts"] is lab["scripts"])

# Change the list inside the deep copy
deep["scripts"].append("lists.py")
print("lab:", lab)
print("deep:", deep)
print(deep == lab)
