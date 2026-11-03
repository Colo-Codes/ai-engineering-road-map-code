# Values and their types
print("https://www.python.org", type("https://www.python.org"))
print(10, type(10))
print(2.5, type(2.5))
print(True, type(True))
print("10", type("10"))  # digits inside quotes

# A variable, bound and then rebound
timeout = 10
print("timeout is", timeout)
timeout = 30
print("timeout is", timeout)
timeout = 2.5
print("timeout is", timeout, type(timeout))

# Arithmetic
print("7 + 2 =", 7 + 2)
print("7 - 2 =", 7 - 2)
print("7 * 2 =", 7 * 2)
print("7 / 2 =", 7 / 2)
print("6 / 2 =", 6 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("7 + 0.5 =", 7 + 0.5)

# Converting between types
timeout_text = "10"
timeout = int(timeout_text)
print(timeout + 5, type(timeout))
print(int(2.9), float("2.5"), str(30))
print(type(str(30)))

# f-strings
url = "https://www.python.org"
print(f"{url} has a timeout of {timeout} seconds")
print(f"Twice the timeout is {timeout * 2} seconds")
