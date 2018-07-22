a_string=input("Enter a string: ")
def sort():
  splitted=a_string.split()
  print(" ".join(sorted(splitted)))

if __name__ == "__main__":
  sort()
