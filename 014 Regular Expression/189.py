import re
from unittest import result

string = "I am learning python from udemy. And this is very good. Also, there are lot of good contents for Python online built by the python community"

search_string = re.search("python", string)
a = re.compile('python')

result = a.findall(string)

print(result)
