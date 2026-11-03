first_run = {200, 404, 500}
second_run = {200, 301}

# Union, intersection and difference
print(first_run | second_run)
print(first_run & second_run)
print(first_run - second_run)
print(second_run - first_run)

# Each operator gives back a new set
both = first_run | second_run
print(both is first_run)
print(first_run, second_run)
