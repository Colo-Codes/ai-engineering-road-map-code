# Two equal lists and a second name for the first list
first = ["values.py", "strings.py"]
second = ["values.py", "strings.py"]
same_list = first
print(id(first), id(second), id(same_list))

# == compares values, is compares objects
print(first == second, first is second)
print(first == same_list, first is same_list)
print(first is not second)

# A copy is equal, but it is a different object
first_copy = first.copy()
print(first_copy == first, first_copy is first)

# After a change, the two separate lists are no longer equal
second.append("lists.py")
print(first == second)
