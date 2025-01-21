""" leap  year """
year = int(input("Enter the year you want to check "))
if year % 4 == 0 :
    print("this is leap year")
elif year % 400 == 0 :
        print("this is leap year")
elif year % 100 == 0 :
      print(" this is not leap year ")
else :
      print ("this is not leap year")