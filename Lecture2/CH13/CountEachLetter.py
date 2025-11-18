def main():
    filename = input("Enter a filename: ").strip()
    # strip() verwijdert spaties links/rechts uit de ingegeven bestandsnaam
    # zodat " test .txt " → "test.txt" wordt
    # dit voorkomt fouten bij open()

    inputFile = open(filename, "r")  # Open the file in read-mode ("r")

    counts = 26 * [0]
    # Maak een lijst met 26 nullen → één plek voor elke letter a–z
    # bv. counts[0] = aantal 'a', counts[1] = aantal 'b', ...

    for line in inputFile:
        # Doorloop elke lijn in het bestand

        # line.lower() zorgt dat hoofdletters (A, B, C) worden omgezet naar kleine letters
        # countLetters telt enkel kleine letters, dus dit is noodzakelijk
        countLetters(line.lower(), counts)

    # Resultaten tonen
    for i in range(len(counts)):
        if counts[i] != 0:  # Alleen letters tonen die effectief voorkwamen
            print(
                chr(ord('a') + i)  # ord('a') = 97, ord('a')+i → ASCII van juiste letter
                + " appears "
                + str(counts[i])
                + (" time" if counts[i] == 1 else " times")
                # enkelvoud vs meervoud
            )

    inputFile.close()  # Bestand sluiten — voorkomen van resource-leaks


# Count each letter in the string
def countLetters(line, counts):
    # line = één lijn uit de file, al in lowercase
    # counts = lijst van 26 tellers die worden bijgewerkt

    for ch in line:
        # per karakter in de lijn:
        if ch.isalpha():
            # Alleen letters tellen (geen cijfers, spaties, leestekens)

            # ord(ch) - ord('a'):
            # voorbeeld: ch = 'c'
            # ord('c') = 99, ord('a') = 97 → index = 2
            # Dit geeft de positie van de letter in het alfabet
            counts[ord(ch) - ord('a')] += 1
            # verhoog de teller voor die letter


main()  # Programma starten
