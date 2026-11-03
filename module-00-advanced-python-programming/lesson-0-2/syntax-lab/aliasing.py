# Two names for one list
scripts = ["values.py", "strings.py"]
same_list = scripts
print("scripts:", scripts)
print("same_list:", same_list)

# Change the list through one name, and both names show the change
same_list.append("lists.py")
print("scripts:", scripts)
scripts[0] = "main.py"
print("same_list:", same_list)

# Two ways to copy a list
scripts_copy = scripts.copy()
scripts_slice = scripts[:]
scripts_copy.append("conditions.py")
scripts_slice[0] = "split_join.py"
print("scripts:", scripts)
print("scripts_copy:", scripts_copy)
print("scripts_slice:", scripts_slice)
