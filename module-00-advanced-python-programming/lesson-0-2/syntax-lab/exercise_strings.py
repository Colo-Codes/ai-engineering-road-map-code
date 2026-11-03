# Starting data: a string with spaces at both ends
heading = "   Weekly REPORT  "
original = heading
print(f"heading: [{heading}]")
print(f"heading is original: {heading is original}")

# Transform `heading`
heading = heading.strip().lower().replace(" ", "-")
print(f"heading: [{heading}]")

# Filename construction
print("------------------------------------")
file_name = f"{heading}.md"
print(f"heading: [{heading}]")
print(f"original: [{original}]")
print(f"file_name: {file_name}, len: {len(file_name)}")
print(
    f"heading == original: {heading == original}, heading is original: {heading is original}"
)
