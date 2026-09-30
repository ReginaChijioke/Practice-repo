import re
string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)

string2 = "".join(char for char in string if char != " ")
print(string2)

string3 = string.replace(" ","")
print(string3)