# Sorteer een lijst in oplopende volgorde (vereenvoudigde versie van Selection Sort)
def selectionSort(lst):

    # We gaan tot het voorlaatste element, want de laatste staat automatisch correct
    for i in range(len(lst) - 1):

        # We zoeken de KLEINSTE waarde in het resterende stuk van de lijst: lst[i:]
        # Dit geeft ons de minimum waarde uit de unsorted zone
        currentMin = min(lst[i:])   # kleinste element vanaf index i tot einde

        # We zoeken de index van dat minimum binnen de volledige lijst
        # lst[i:].index(currentMin) geeft de positie *binnen het stuk lst[i:]*,
        # dus we tellen i erbij om de echte index in de volledige lijst te krijgen.
        currentMinIndex = i + lst[i:].index(currentMin)

        # Als de kleinste waarde NIET op positie i staat, moeten we wisselen
        if currentMinIndex != i:

            # Swap met tuple assignment:
            # Het element op positie currentMinIndex wisselen we met lst[i]
            lst[currentMinIndex], lst[i] = lst[i], currentMin

        print(lst)  # Print de lijst na elke volledige selectie-stap (visualisatie)

def main():
    lst = [-2, 4.5, 5, 1, 2, -3.3]
    selectionSort(lst)


main()