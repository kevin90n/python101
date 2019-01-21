# Reverse a string

def reverse():
  reversed=""
  string=input("enter a string below to get it reversed:  ")
  k = len(string) - 1
  for i in range(0,len(string)):
    reversed = reversed + string[k]
    k-=1
  return reversed

if __name__ == '__main__':
  print("We're going to reverse a string now")
  x=reverse()
  print(x)
