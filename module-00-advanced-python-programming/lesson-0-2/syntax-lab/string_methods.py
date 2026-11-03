# Changing case
phrase = "values and types"
print(phrase.upper())
print(phrase.title())
print("Values AND Types".lower())

# Removing whitespace from the ends
padded = "   lesson-0-2   "
print(f"[{padded.strip()}]")
print(f"[{padded.lstrip()}]")
print(f"[{padded.rstrip()}]")

# Methods that take an argument
print("lesson-0-2".removeprefix("lesson-"))
print("syntax-lab".removesuffix("-lab"))

# The original string stays the same
command = "uv run main.py"
new_command = command.replace("main.py", "values.py")
print("command:", command)
print("new_command:", new_command)
print(f"padded: [{padded}]")

# Rebinding the name to the result
command = command.replace("main.py", "values.py")
print("command:", command)
