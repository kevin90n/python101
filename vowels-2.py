#Count vowles in python string

vowel=['a','e','i','o','u']

def vowels():
  cnt=0
  string=input("Enter a string to count the number of vowels in it: ")
  for i in vowel:
   cnt+=string.count(i) 
  return cnt
  

if __name__ == '__main__':
  print("We will be counting vowels")
  x = vowels()
  print(x)
