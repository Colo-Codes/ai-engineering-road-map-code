# 0 is a real value, and None means there is no value
settings = {"url": "https://www.python.org", "retries": 0}
retries = settings.get("retries")
timeout = settings.get("timeout")
print("retries:", retries, "timeout:", timeout)

# not treats 0 and None the same way
print(not retries, not timeout)

# is None tells them apart
print(retries is None, timeout is None)

# or replaces every falsy value, including 0 and ""
print(retries or 3, timeout or 3)
label = ""
print(f"[{label or 'unnamed'}]")

# An is None check replaces only None
if retries is None:
    retries = 3
if timeout is None:
    timeout = 3
print("retries:", retries, "timeout:", timeout)
