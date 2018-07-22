def setpunc():
  a_string=input("Enter a string with punctuations: ")
  punctuations=list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
  length=(len(punctuations))
  for i in range(0, length):
    if punctuations[i] in a_string:
      final_string=a_string.replace(punctuations[i], "")
      a_string=final_string
    else:
      final_string=a_string
    i+=1  
  print(final_string)
if __name__=="__main__":
  setpunc()
