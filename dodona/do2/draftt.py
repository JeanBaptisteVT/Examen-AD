def woorden_splitsen(tekstfile):
    f = open(tekstfile, 'r')
    woorden = []


    for line in f:
        new_line = " "
        for ch in line:
            if ch.isalpha():
                new_line += ch
            else:
                new_line += " "

        for woord in new_line.split():
            woorden.append(woord)

    f.close()
    return woorden

def woorden_tellen(tekstfile):
    woorden = woorden_splitsen(tekstfile)
    telling = {}

    for woord in woorden:
        woord = woord.lower()
        if woord in telling:
            telling[woord] += 1
        else:
            telling[woord] = 1
    return telling
