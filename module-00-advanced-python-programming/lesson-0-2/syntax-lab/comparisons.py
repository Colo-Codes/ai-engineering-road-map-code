# Comparing numbers
status_code = 404
print(status_code == 200, status_code != 200)
print(status_code < 500, status_code >= 400, status_code > 404)
print(10 == 10.0, 10 == "10")

# Keeping a result in a variable
found = status_code == 404
print(found, type(found))

# Comparing strings
file_name = "README.md"
print(file_name == "readme.md")
print(file_name.lower() == "readme.md")
print(file_name)

# in and not in
command = "uv run --locked main.py"
print("--locked" in command, "--Locked" in command)
scripts = ["values.py", "strings.py", "main.py"]
print("main.py" in scripts, "lists.py" not in scripts)
print("main" in scripts)
