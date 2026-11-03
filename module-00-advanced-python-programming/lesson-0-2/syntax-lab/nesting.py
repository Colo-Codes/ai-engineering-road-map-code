# A list inside a dictionary
lab = {
    "name": "syntax-lab",
    "scripts": ["values.py", "strings.py"],
}
print(lab["scripts"])
print(lab["scripts"][0])
lab["scripts"].append("lists.py")
print(lab)

# Dictionaries inside a list
results = [
    {"url": "https://www.python.org", "status": 200},
    {"url": "https://www.python.org/missing", "status": 404},
]
print(results[1])
print(results[1]["status"], len(results))

# A dictionary inside a dictionary
lab_info = {
    "name": "syntax-lab",
    "python": {"major": 3, "minor": 13},
}
print(lab_info["python"])
print(lab_info["python"]["minor"])
