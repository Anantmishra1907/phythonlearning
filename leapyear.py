"""To check the given year is a leap year """
year  = int (input(" Enter the year : "))
if year % 4 == 0 :
     print(" This is leap year ")
elif year %100  != 0:
    print("This is not a leap year ")
elif year % 400 == 0 :
   print("This is lep year ")
else :
    print("This is not leap year ")
