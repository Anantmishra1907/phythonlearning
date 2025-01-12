'''To check whether  a  given number is palindrome or not '''
num = int(input("Enter the number tio check whether the number is palindrome or not : "))
rev = 0
temp = num
while temp > 0 :
    last = temp % 10 
    rev = rev*10+last
    temp = temp // 10 
if num == rev :
    print("Palindrome")
else :
    print("Not the Palindrome ")