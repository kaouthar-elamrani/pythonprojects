def reverse_string(string1):
  string2=""
  for letter in string1:
    string2=letter+string2
  return string2

string1=str(input("string1"))
string2=reverse_string(string1)
print(string2)
