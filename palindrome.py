a_string = input("Enter a string: ")
final_string=[]

def reversing():
  splitted=list(a_string)
  i=(len(a_string)) - 1
  j = 0
  while( i >= 0 ):
    if (splitted[i] != splitted[j]):
          final_string.append("failed")
    j=j+1
    i=i-1
#  print(final_string)
  if final_string != []:
    print("Not a palindrome")
  else:
    print("It is a palindrome")
if __name__ == "__main__":
  reversing()
