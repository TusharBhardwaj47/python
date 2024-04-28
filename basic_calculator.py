# Simple calculator
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  if y == 0:
    return "Error"
  else:
    return x / y
print("Choose operation : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
  ch = input("Enter choice(1/2/3/4): ")
  if ch in ('1', '2', '3', '4'):
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
     if ch == '1':
          print(f"The result is {add(num1, num2)}")
     elif ch == '2':
          print(f"The result is {subtract(num1, num2)}")
     elif ch == '3':
          print(f"The result is {multiply(num1, num2)}")
     elif ch == '4':
          print(f"The result is {divide(num1, num2)}")
          nex = input(" Next calculation ? (yes/no): ")
          if nex!= 'yes':
                break
  else:
      print("Invalid Input")