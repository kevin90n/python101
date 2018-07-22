height=float(input("Enter your height in meters: "))
weight=int(input("Enter your weight in KG: "))
def bmicalculator():
  bmi=float((weight/height)/height)
  print("Your BMI is", bmi)
  if bmi < 18.5:
    print("You are underweight")
  if bmi > 18.5 and bmi < 25.0:
    print("Normal weight")
  if bmi > 25.0:
    print("You are fat!!")
if __name__=="__main__":
  bmicalculator()
 
  


