# Two places where None appears
settings = {"url": "https://www.python.org", "timeout": 10}
missing = settings.get("retries")
scripts = ["values.py", "strings.py", "main.py"]
sort_result = scripts.sort()
print(missing, sort_result)
print(type(missing), bool(missing))

# There is only one None object
print(missing is sort_result)
print(missing is None, sort_result is None)

# is not None: the key "timeout" is in the dictionary
timeout = settings.get("timeout")
print(timeout is None, timeout is not None)
