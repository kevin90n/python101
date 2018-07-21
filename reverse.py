a_string = input("Enter a string: ")
final_string=[]

def reversing():
  splitted=list(a_string)
  i=(len(a_string)) - 1
  while (i >= 0):
    final_string.append(splitted[i])
    i-=1
  print("".join(final_string))
if __name__ == "__main__":
  reversing()
