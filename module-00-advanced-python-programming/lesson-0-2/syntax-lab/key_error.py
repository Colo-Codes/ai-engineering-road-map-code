settings = {"url": "https://www.python.org", "timeout": 10}
print("timeout:", settings["timeout"])
# print("retries:", settings["retries"])
print("retries:", settings.get("retries", 0))
