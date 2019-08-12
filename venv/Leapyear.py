y = int(input("Year = "))
y400 = y%400
y100 = y%100
y4 = y%4

if (y400 == 0):
    print("It is leap year")
elif (y100 == 0):
    print("It's not Leap Year at 100")
elif (y4 == 0):
    print("It's Leap Year, Enjoy your one day extra")
else:
    print("It's not Leap Year")
    
