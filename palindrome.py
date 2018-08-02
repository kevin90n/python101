import sys
entries=sys.argv[1]
length=int(len(entries) -1)
i=0
result=None
while( i < length):
  print(entries[i])
  print(entries[length])
  if entries[i] != entries[length]:
    result="nope"
  i+=1
  length-=1
if(result!=None):
 print("not a palindrome")
else:
  print("palindrome")

    
    
