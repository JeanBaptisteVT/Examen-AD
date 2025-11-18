def main():
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    # .strip() verwijdert spaties links/rechts zodat "  test.txt  " → "test.txt" wordt

    inputFile = open(filename, "r")  # Open the file in read-mode ("r")

    wordCounts = {}   # lege dictionary: woord → aantal keer dat het voorkomt

    for line in inputFile:
        # per lijn:
        #   - lower(): hoofdletters omzetten naar kleine letters
        #   - processLine telt de woorden in deze lijn
        processLine(line.lower(), wordCounts)

    inputFile.close()   # bestand sluiten

    # wordCounts.items() geeft lijst van (woord, aantal)-paren
    pairs = list(wordCounts.items())   # bv. [('the', 5), ('test', 3), ...]

    # Hier draaien we elk paar om → zodat de count eerst komt
    # items wordt dan bv.: [[5,'the'], [3,'test'], ...]
    # Waarom? omdat sort() dan automatisch op het getal sorteert
    items = [[x, y] for (y, x) in pairs]

    # sort() sorteert oplopend op het eerste element (dus op frequentie)
    items.sort()

    # We lopen van achter naar voor (dus van hoogste frequentie naar laagste)
    for i in range(len(items) - 1, 0, -1):
        # items[i] = [aantal, woord]
        # print: woord <tab> aantal
        print(items[i][1] + "\t" + str(items[i][0]))


# Count each word in the line
def processLine(line, wordCounts):
    # line = de inhoud van 1 lijn in lowercase
    # replacePunctuations verwijdert speciale tekens en vervangt ze door spaties
    line = replacePunctuations(line)

    # split() splitst de lijn op spaties → lijst van woorden
    words = line.split()

    for word in words:
        # als het woord al in dictionary staat → verhoog counter
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            # zoniet: nieuw woord toevoegen met count = 1
            wordCounts[word] = 1


# Replace punctuations in the line with space
def replacePunctuations(line):
    # per karakter in line → als het een speciaal tekentje is → vervang door spatie
    for ch in line:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            # line.replace(ch," ") vervangt ALLE voorkomen van dit karakter
            line = line.replace(ch, " ")

    return line


main()  # start main
