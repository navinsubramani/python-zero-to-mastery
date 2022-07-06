import re

string = "I am learning python from udemy. And this is very good. Also, there are lot of good contents for Python online built by the python community"

# https://regex101.com/
pattern = re.compile(r"[a-zA-Z].[t]")

a = pattern.search(string)

print(a)
