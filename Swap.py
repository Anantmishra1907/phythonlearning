'''Swapping of two Numbers '''
x = int (input("Enter first number"))
y = int (input("Enter Second number"))
print("Before Swapping X : ", x  , "Y : ", y)

temp = x
x = y
y = temp 
print("After Swapping X:", x ,"Y :",y)
''' Without using third variables'''
x = int (input("Enter first number"))
y = int (input("Enter Second number"))
print("Before Swapping X : ", x  , "Y : ", y)
x = x+y
y = x - y
x = x - y
print("After Swapping X:", x ,"Y :",y)



