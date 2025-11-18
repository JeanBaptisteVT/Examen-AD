def woorden_splitsen(bestandsnaam):
    woorden = []
    f = open(bestandsnaam, "r")

    for regel in f:
        nieuwe_regel = ""
        for char in regel:
            if char.isalpha():           # letter
                nieuwe_regel += char
            else:                        # geen letter
                nieuwe_regel += " "
        # split op spaties en voeg toe
# heel die for loop is gewoon zorgen dat alle symbolen die geen letter zijn een spatie worden
# nieuwe regel is dus die vervanging van die oude zonder die symbolen
# dan splitten we die nieuwe regel en voegen we de woorden toe aan onze lijst
        for woord in nieuwe_regel.split():
            woorden.append(woord)

    f.close() #niet vergeten om de file te sluiten
    return woorden

def woorden_tellen(bestandsnaam):
    woorden = woorden_splitsen(bestandsnaam)
    telling = {}

    for woord in woorden:
        woord = woord.lower()
        if woord in telling:
            telling[woord] += 1
        else:
            telling[woord] = 1

    return telling



