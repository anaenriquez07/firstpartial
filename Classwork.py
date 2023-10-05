def suma(a,b):
  x = a + b 
  return x

def resta (a,b):
  x = a - b 
  return x

print ("Dame el primer número:")
a = int(input())
print ("Dame el segundo número:")
b = int(input())
print ("La suma da ",suma(a,b), "Y la resta da ",resta(a,b))

def multiplication(a,b):
  x = a*b
  return x

def division (a,b):
  x = a/b
  return x

print ("Give me the first number:")
a = int(input())
print ("Give me the second number:")
b = int(input())
print("The multiplication is equal to ",multiplication(a,b))
print("And the division is ",division(a,b))


def conversion(k):
  km = k * 1000
  return km
  
print ("How many kilometers")
k = int(input())
print ("The amount of kilometers to meters is ",conversion(k))


def triangle_area(h,b):
  x = (int(h) * int(b)) / 2
  return x
print ("What is the height?")
h = int(input())
print ("What is the base?")
b = int(input())
print ("The area of your triangle is",triangle_area(h,b))
