# A dictionary with three keys
settings = {"url": "https://www.python.org", "timeout": 10, "follow_redirects": True}
print(settings)
print(type(settings), len(settings))

# Reading a value by its key
print(settings["url"])
print(settings["timeout"] * 2)

# Changing a value and adding a key
settings["timeout"] = 30
settings["retries"] = 3
print(settings, len(settings))

# Removing a key and its value
del settings["follow_redirects"]
print(settings)

# in checks the keys
print("timeout" in settings, 30 in settings)
print("follow_redirects" not in settings)

# An empty dictionary, filled one key at a time
limits = {}
limits["timeout"] = 10
print(limits, len(limits))
