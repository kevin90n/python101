a_string=input("Enter a string: ")
vowels=['a','e','i','o','u']
count=0
for i in range(0,5):
  count=count+(a_string.count(vowels[i]))
print( "Total number of vowels are", count )
