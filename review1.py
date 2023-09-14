def d():
  print ("What is your height in meters?")
  height = input()
  print ("How much do you weight in kg?")
  weight = input()
  result = float(weight)/float(height)**2
  if (result < 18.5): print ("Your BMI is",result), print ("You are underweight")
  if (18.5 < result < 24.9): print ("Your BMI is",result), print ("You are healthy")
  if (25.0 < result < 29.9): print ("Your BMI is",result), print ("You are overweight")
  if (30.0 < result): print ("Your BMI is",result), print ("You are obese")
  
d()
