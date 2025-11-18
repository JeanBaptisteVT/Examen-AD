def mergeSort(list):  # we delen de lijst in 2
    if len(list) > 1: # we doen dit tot we allemaal aparte elementen hebben

        # we starten met de eerste helft, we splitten op recursieve wijze de eerste helft op in
        # allemaal eenheden, dan gaan we die lijst met die eenheden gaan mergesorten
        firstHalf = list[ : len(list) // 2]
        mergeSort(firstHalf)

        # idem voor tweede helft
        # Merge sort the second half
        secondHalf = list[len(list) // 2 : ]
        mergeSort(secondHalf)

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, list)


# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1 (linker gesorteerde helft)
    current2 = 0  # Current index in list2 (rechter gesorteerde helft)
    current3 = 0  # Current index in temp (de samengevoegde lijst)

    # Zolang er elementen in BEIDE lijsten zitten
    # vergelijken we het eerstvolgende element van list1 en list2.
    # We kiezen telkens het kleinste element en plaatsen dat in temp.
    while current1 < len(list1) and current2 < len(list2):

        # Vergelijk het eerstvolgende element uit elke helft
        if list1[current1] < list2[current2]:
            # Het element uit list1 is kleiner:
            # -> plaats het in temp, want we vullen temp OPLOPEND
            temp[current3] = list1[current1]
            current1 += 1          # ga naar het volgende element in list1
            current3 += 1          # temp is één plaats verder gevuld

        else:
            # Element uit list2 is kleiner of gelijk:
            # -> dat vullen we nu in temp
            temp[current3] = list2[current2]
            current2 += 1          # ga naar het volgende element in list2
            current3 += 1          # temp schuift 1 op

    # ALS één van de twee lijsten op is,
    # dan blijft de andere lijst nog elementen over hebben.
    # Die zijn AL gesorteerd, dus we kunnen ze gewoon rechtstreeks kopiëren.

    # Nog elementen over in list1?
    while current1 < len(list1):
        temp[current3] = list1[current1]  # place entire rest of list1
        current1 += 1
        current3 += 1

    # Nog elementen over in list2?
    while current2 < len(list2):
        temp[current3] = list2[current2]  # place entire rest of list2
        current2 += 1
        current3 += 1


def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(list)
    for v in list:
        print(v, end = " ")

main()
