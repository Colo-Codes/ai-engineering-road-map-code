settings = {"url": "https://www.python.org", "timeout": 10}

# .get() with and without a default
print(settings.get("timeout"), settings.get("timeout", 5))
print(settings.get("retries", 0))
print(settings.get("retries"))
print(settings)

# Keys, values and items
print(settings.keys())
print(settings.values())
print(settings.items())

# list() turns each of them into a list
keys = list(settings.keys())
print(keys, keys[0])
pairs = list(settings.items())
print(pairs[1], type(pairs[1]))
