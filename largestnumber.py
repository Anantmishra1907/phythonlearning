''' To check the greatest number among three using elif  '''
x = int (input(" Enter the first number : "))
y = int (input(" Enter the second number : "))
z = int (input(" Enter the third  number : "))
if x > y and x > z :
    print("This number  is greater ", x)
elif y > x and y > z :
    print("This number is greater ", y)
else :
    print("This number is greatest of all  ", z)
""" Using nested  if else """
x = int (input(" Enter the first number : "))
y = int (input(" Enter the second number : "))
z = int (input(" Enter the third  number : "))
if x > y :
    if x > z:
          print("This number  is greater ", x)
    else :
         print("This number is greatest of all  ", z)
else :
     if y >  z :
          print("This number  is greater ", y)
     else :
          print("This number is greatest of all  ", z)


""" Using terniray Operator"""
