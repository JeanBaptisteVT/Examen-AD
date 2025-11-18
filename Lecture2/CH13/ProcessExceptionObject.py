try:
    number = float(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception:", ex)
#met die ex zie je de boodschap van de exception, wat is die exception juist?

