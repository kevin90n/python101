a_string=input("Enter a string: ")
string = "".join(reversed(a_string))
if(a_string == string):
  print("It is a palindrome")
else:
  print("not a palindrome")
