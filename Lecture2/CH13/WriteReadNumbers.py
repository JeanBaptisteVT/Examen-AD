from random import randint 

def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w")
    for i in range(10):
        outputFile.write(str(randint(0, 9)) + " ") #we voegen een random getal toe maar we zetten het eerst om naar een string
    outputFile.close() # Close the file

    # Open file for reading data
    inputFile = open("Numbers.txt", "r")
    s = inputFile.read() # Read all data to s
    numbers = [int(x) for x in s.split()] #we splitten die reeks om een list te bekomen
    #float/int niet vergeten, anders werken we met text en kunnen we geen bewerkingen doorvoeren
    for number in numbers:
        print(number, end = " ")
    inputFile.close() # Close the file
    
main() # Call the main function
