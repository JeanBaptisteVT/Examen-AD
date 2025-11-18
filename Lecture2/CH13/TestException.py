def main():
    try:
        number1 = int(input("Enter an integer: "))      
        number2 = int(input("Enter an integer: "))      
        result = number1 / number2
        print("Result is " + str(result))
    except ZeroDivisionError: # Catch zero divisor error
        print("Division by zero!")
    except:
        print("Something wrong in the input")
    else: #else enkel uitgevoerd als de exceptions niet zijn uitgevoerd
        print("No exceptions")
    finally: #altijd uitgevoerd
        print("The finally clause is executed")

main()