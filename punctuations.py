a_string=input("Enter a string with punctuations: ")
punctuations=list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
print(punctuations)
length=(len(punctuations))
for i in range(0, length):
  if punctuations[i] in a_string:
    final_string=a_string.replace(punctuations[i], "")
    a_string=final_string
  i+=1  
print(final_string)
