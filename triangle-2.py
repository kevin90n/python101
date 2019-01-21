import sys 

def triangle(pattern):
  for i in range(1,20):
    print(pattern*i)
  

if __name__ == "__main__":
  print(" We are going to make a triangle shape ")
  if(len(sys.argv) < 2):
    print("Enter a pattern")
  else:
    triangle(sys.argv[1])

