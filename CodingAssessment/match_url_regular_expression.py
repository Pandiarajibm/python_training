import re

text = "https://www.example.com/page_123.html"
match = re.match(r'(http[s]?://[a-z./A-Z_0-9]+)', text)

if match:
    print(f"Found URL: {match.group(1)}")
else:
    print("No URL found at the beginning of the string.")

