def bubbleSort(lst):
    needNextPass = True  # Dit bepaalt of we nog een extra ronde moeten doen
    # Als in een volledige pass geen enkele swap gebeurt, (een pass is 1 keer de volledige reeks overlopen)
    # betekent dit dat de lijst al volledig gesorteerd is.

    k = 1  # k telt hoeveel elementen al 'vanachter' vaststaan
    # De laatste k elementen zijn al in hun juiste plaats
    # want bubble sort duwt de grootste elementen naar achter.

    while k < len(lst) and needNextPass:
        needNextPass = False  # We gaan ervan uit dat de lijst al gesorteerd is
        # Als we toch een swap doen → moet er nog een pass komen

        # We vergelijken telkens twee buur-elementen: lst[i] en lst[i+1]
        # We stoppen op len(lst) - k omdat het einde al "gesorteerd" is
        for i in range(len(lst) - k):

            # Als het linker element groter is dan het rechter → verkeerd om → we wisselen
            if lst[i] > lst[i + 1]:
                # swap lst[i] and lst[i + 1]
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                # Omdat we een swap hebben gedaan, is de lijst nog niet gesorteerd
                needNextPass = True

        k += 1  # Na elke volledige pass staat het grootste element op het einde
        # dus we hoeven dat deel niet meer te bekijken


def main():
    lst = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")

main()

# k = 1 omdat Bubble Sort altijd vergelijkt t.e.m. len(lst)-1
# in de eerste pass. Als k = 0 zou zijn, krijg je een indexfout.
# k bepaalt de limiet van de loop, NIET hoeveel elementen al gesorteerd zijn.