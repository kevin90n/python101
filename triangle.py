a_string=input("Enter a symbol you want in triangle: ")
a_length=int(input("Enter how big you want it (In number of lines): "))
def triangle():
  j=1
  for i in range(0, a_length):
    if( j <= a_length):
      print(a_string * j)
      j+=1

if __name__=="__main__":
  triangle()
  
