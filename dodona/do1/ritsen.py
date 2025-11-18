def samenvoegen(lijst1, lijst2):
    lijst3 = []  # nieuwe lijst die de samengevoegde elementen bevat

    # we itereren maar tot de lengte van de kortste lijst
    for i in range(min(len(lijst1), len(lijst2))):
        lijst3.append(lijst1[i])  # voeg element uit lijst1 toe
        lijst3.append(lijst2[i])  # voeg element uit lijst2 toe

    return lijst3


def weven(lijst1, lijst2):
    lijst3 = []

    # we gaan tot de lengte van de langste lijst
    for i in range(max(len(lijst1), len(lijst2))):

        # i % len(lijst1): als i groter wordt dan lengte lijst1,
        #                  start je opnieuw van index 0 (circulair)
        lijst3.append(lijst1[i % len(lijst1)])

        # idem voor lijst2
        lijst3.append(lijst2[i % len(lijst2)])

    return lijst3

def ritsen(lijst1, lijst2):
    lijst3 = []

    # basisritsen: zo lang beide lijsten nog elementen hebben
    for i in range(min(len(lijst1), len(lijst2))):
        lijst3.append(lijst1[i])
        lijst3.append(lijst2[i])

    # Bepaal waar de rits stopte:
    stop = min(len(lijst1), len(lijst2))

    # als lijst1 langer is, voeg de rest toe
    if len(lijst1) > stop:
        lijst3.extend(lijst1[stop:])   # neem de rest van lijst1

    # als lijst2 langer is, voeg de rest toe
    elif len(lijst2) > stop:
        lijst3.extend(lijst2[stop:])   # neem de rest van lijst2

    return lijst3
