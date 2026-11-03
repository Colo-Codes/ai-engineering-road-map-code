# Two names for one tuple
version = (3, 13, 15)
old_version = version
print(version is old_version)

# Rebinding: version refers to a new tuple
version = (3, 14, 0)
print("version:", version)
print("old_version:", old_version)
print(version is old_version)
