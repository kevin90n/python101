a_string=input("enter a string: ")
vowels=['a','e','i','o','u']
def findvowels():
  count=0
  check_string=list(a_string)
  for i in range(0,5):
    for j in range(0, len(a_string)):
      if vowels[i] == check_string[j]:
        count+=1
  
  print(" Total count of vowels", count)

if __name__ == "__main__":
  findvowels()


