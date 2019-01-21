import sys
def check_pal(string):
  k=0
  g=len(string) -1
  Not=0
  for i in range(0, len(string)):
    if string[k] == string[g]:
      k+=1
      g-=1
    else:
      Not = 1
  if Not == 1:
    print("not palindrome")
  else:
    print("palindrome")

if __name__ == "__main__":
  if len(sys.argv[1:]) < 1:
    print("ERROR\t:exitting...... arguments passed")
    sys.exit()
  else:
    check_pal(sys.argv[1])   
