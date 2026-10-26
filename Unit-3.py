with open("sample.text", "r") as file:
    lines = file.readlines()

# Find the longest line
longest_line = max(lines, key=len)

# Find line number
line_number = lines.index(longest_line) + 1

# Display result
print("Longest line:", longest_line.strip())
print("Line number:", line_number)
print("Length:", len(longest_line.strip()))
