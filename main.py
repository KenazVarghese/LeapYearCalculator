
year = int(input("Which year do you want to check? "))

if (round(year/4))/1 == year/4:

    if (round(year/100))/1 == year / 100:
        if (round(year/400))/1 == year / 400:
            print("Leap year.")
        else:
            print("Not leap year")
    else: 
        print("Leap year.")
else:
    print("Not leap year.")
