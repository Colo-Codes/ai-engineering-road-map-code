# and, or and not with True and False
print(True and True, True and False)
print(False or True, False or False)
print(not True, not False)

# Combining comparisons
status_code = 404
print(status_code >= 400 and status_code < 500)
print(status_code == 200 or status_code == 404)
print(not status_code == 200)

locked = True
print(locked and status_code == 200)
