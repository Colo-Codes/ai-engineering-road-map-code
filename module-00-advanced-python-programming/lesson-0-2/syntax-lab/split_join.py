# From a string to a list
command = "uv run --locked main.py"
words = command.split()
print(words, len(words))
print(command)

version = "3.13.15"
parts = version.split(".")
print(parts)
print(parts[0], parts[-1])

# From a list to a string
words[-1] = "values.py"
print(" ".join(words))
print("-".join(["lesson", "0", "2"]))
