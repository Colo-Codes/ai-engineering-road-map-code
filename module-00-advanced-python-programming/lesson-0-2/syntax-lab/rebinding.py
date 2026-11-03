# Mutation: the list changes, and both names show the change
scripts = ["values.py", "strings.py"]
same_list = scripts
scripts.append("lists.py")
print("scripts:", scripts)
print("same_list:", same_list)

# Rebinding: scripts refers to a new list
scripts = ["main.py"]
print("scripts:", scripts)
print("same_list:", same_list)
