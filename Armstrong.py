'''Program to check whether a number is the armstrong or not '''
num = int(input("Enter the number to check Aramstrong "))
sum = 0 
n = num
while (n > 0 ):
    d = n % 10
    sum = sum + int(d)**3
    n = n/10
if num == sum :
    print("Armstrong ")
else :
    print("Not the armstrong ")
