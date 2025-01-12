'''To give fibonnaci series '''
num = int(input("Enter the number :  "))
n0 , n1 = 0 , 1 
if num <= 0 :
    print("Enter the positive number ")
elif num == 1 :
    print(n0)
else :
    print(n0 , n1)
    for i in  range  (3 , num+1):
        nth = n0 + n1 
        print(nth)
        n0 = n1
        n1 = nth


