def InsertionSort(lst):

    # We beginnen op index 1 omdat lst[0] vanzelf "gesorteerd" is (1 element kan je niet vergelijken met andere)
    for i in range(1, len(lst)):

        # Het element dat we willen invoegen in het gesorteerde deel links van i
        currentElement = lst[i]

        # k wijst naar de laatste index van het gesorteerde gedeelte (0 .. i-1)
        k = i - 1

        # Schuif alle elementen die groter zijn dan currentElement één positie naar rechts
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]   # element naar rechts duwen
            k -= 1                # ga verder naar links

        # Plaats het element in het vrijgekomen 'gaatje'
        lst[k + 1] = currentElement

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    InsertionSort(list)
    for v in list:
        print(v, end = " ")

main()
