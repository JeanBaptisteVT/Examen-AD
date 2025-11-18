"""
file_handling_cheatsheet.py

Overzicht van:
- Text files openen / lezen / schrijven
- Modes: r, w, a, rb, wb
- getallen lezen/schrijven
- os.path.isfile gebruiken
- try / except / else / finally
- exceptions met 'as' en custom exceptions
- (optioneel) webpagina lezen met urllib.request

Gebruik dit bestand als referentie tijdens het studeren / examen.
"""

import os.path
import urllib.request


# ---------------------------------------------------------
# 1. BASIS: text file schrijven (write) en lezen (read)
# ---------------------------------------------------------

def demo_write_text_file():
    # "w" = write mode
    # Als bestand al bestaat → inhoud wordt OVERSCHREVEN
    # Als het niet bestaat → wordt het aangemaakt
    f = open("demo_text.txt", "w")

    # write() neemt ENKEL strings
    f.write("Eerste lijn\n")
    f.write("Tweede lijn\n")
    f.write("Derde lijn\n")

    f.close()  # altijd sluiten


def demo_read_text_file():
    # "r" = read mode
    # Bestand moet bestaan, anders krijg je FileNotFoundError
    f = open("demo_text.txt", "r")

    # Volledige inhoud als één string
    content = f.read()
    print("VOLLEDIGE INHOUD MET read():")
    print(content)

    f.close()


# ---------------------------------------------------------
# 2. Regel per regel lezen: readline() en readlines()
# ---------------------------------------------------------

def demo_read_line_by_line():
    f = open("demo_text.txt", "r")

    print("LEZEN MET readline():")
    line = f.readline()  # leest 1 lijn per keer
    while line != "":
        print("Lijn:", line.rstrip("\n"))
        line = f.readline()

    f.close()

    print("\nLEZEN MET readlines():")
    f = open("demo_text.txt", "r")
    lines = f.readlines()  # lijst van alle lijnen
    for idx, line in enumerate(lines):
        print(f"Lijn {idx}:", line.rstrip("\n"))
    f.close()


# ---------------------------------------------------------
# 3. Append-mode: "a" (toevoegen aan het einde)
# ---------------------------------------------------------

def demo_append_text_file():
    # "a" = append
    # Schrijft aan het einde van het bestand
    f = open("demo_text.txt", "a")
    f.write("Lijn toegevoegd in append-mode\n")
    f.close()


# ---------------------------------------------------------
# 4. Getallen schrijven en opnieuw inlezen
# ---------------------------------------------------------

def demo_write_numbers():
    f = open("Numbers.txt", "w")
    # Getal → naar string omzetten met str()
    f.write(str(10) + " " + str(20) + " " + str(30) + "\n")
    f.close()


def demo_read_numbers():
    f = open("Numbers.txt", "r")

    line = f.readline()      # bv. "10 20 30\n"
    parts = line.split()     # ["10", "20", "30"]
    numbers = [int(p) for p in parts]  # [10, 20, 30]
    print("Ingelezen getallen:", numbers)

    f.close()


# ---------------------------------------------------------
# 5. Checken of een file bestaat: os.path.isfile
# ---------------------------------------------------------
#import os.path niet vergeten
def demo_check_file_exists(filename):
    if os.path.isfile(filename):
        print(f"Bestand '{filename}' bestaat.")
    else:
        print(f"Bestand '{filename}' bestaat NIET.")


# ---------------------------------------------------------
# 6. try / except rond file open
# ---------------------------------------------------------

def demo_try_except_open():
    filename = "mogelijk_bestaat_het_niet.txt"

    try:
        f = open(filename, "r")
        content = f.read()
        print(f"Inhoud van {filename}:")
        print(content)
        f.close()

    except FileNotFoundError:
        # Specifieke except voor "bestand niet gevonden"
        print(f"Fout: bestand '{filename}' werd niet gevonden.")

    except PermissionError:
        # Specifieke except voor "geen rechten"
        print(f"Fout: geen toegang tot bestand '{filename}'.")

    except Exception as ex:
        # Algemene except (alle andere fouten)
        print("Er trad een onverwachte fout op:", ex)


# ---------------------------------------------------------
# 7. try / except / else / finally
# ---------------------------------------------------------

def demo_try_except_else_finally():
    filename = "demo_text.txt"

    f = None
    try:
        f = open(filename, "r")
        # Als dit lukt, gaan we naar 'else'
    except FileNotFoundError:
        print(f"[try/except] Bestand '{filename}' niet gevonden.")
    else:
        # Dit blok wordt ALLEEN uitgevoerd als er GEEN except gebeurde
        print("[else] Bestand succesvol geopend, lezen...")
        print(f.read())
    finally:
        # Dit blok wordt ALTIJD uitgevoerd, zelfs bij fouten
        if f is not None:
            f.close()
            print("[finally] Bestand is gesloten.")


# ---------------------------------------------------------
# 8. Exception object gebruiken: 'as ex'
# ---------------------------------------------------------

def demo_exception_object():
    try:
        x = 1 / 0
    except ZeroDivisionError as ex:
        # 'ex' bevat de foutbeschrijving
        print("Er gebeurde een ZeroDivisionError:", ex)


# ---------------------------------------------------------
# 9. Zelf exceptions opwerpen met raise
# ---------------------------------------------------------

class InvalidRadiusException(Exception):
    """Custom exception type voor ongeldige radius."""
    pass


def compute_circle_area(r):
    # Stel: negatieve radius is niet toegelaten
    if r < 0:
        # We gooien een zelfgekozen exception met een boodschap
        raise InvalidRadiusException("Radius moet >= 0 zijn.")

    from math import pi
    return pi * r * r


def demo_raise_custom_exception():
    try:
        print("Oppervlakte met r=2:", compute_circle_area(2))
        print("Oppervlakte met r=-5:", compute_circle_area(-5))
    except InvalidRadiusException as ex:
        print("Ongeldige radius:", ex)


# ---------------------------------------------------------
# 10. Webpagina lezen met urllib.request (optioneel hoofdstukdeel)
# ---------------------------------------------------------
#import urllib.request niet vergeten
def demo_read_webpage():
    # Dit werkt enkel met internet.
    # urllib.request.urlopen geeft een "file-like object" terug.
    try:
        response = urllib.request.urlopen("https://example.com")
        data = response.read()       # bytes
        text = data.decode()         # omzetten naar string
        print("Eerste 200 characters van webpagina:")
        print(text[:200])
    except Exception as ex:
        print("Kon webpagina niet ophalen:", ex)

#na hier boeit niet
# ---------------------------------------------------------
# 11. Binary files (kort voorbeeld: schrijven en lezen)
# ---------------------------------------------------------

def demo_binary_file():
    # "wb" = write binary
    with open("demo_binary.bin", "wb") as f:
        # bytes schrijven (b'' literal)
        f.write(b"Hello in binary\n")

    # "rb" = read binary
    with open("demo_binary.bin", "rb") as f:
        data = f.read()
        print("Inhoud van demo_binary.bin (bytes):", data)


# ---------------------------------------------------------
# main: enkel runnen als script direct uitgevoerd wordt
# ---------------------------------------------------------

def main():
    print("=== DEMO FILE HANDLING & EXCEPTIONS ===")

    print("\n1) Schrijven naar text file:")
    demo_write_text_file()

    print("\n2) Text file lezen (read):")
    demo_read_text_file()

    print("\n3) Regel per regel lezen:")
    demo_read_line_by_line()

    print("\n4) Append-mode:")
    demo_append_text_file()
    demo_read_text_file()

    print("\n5) Getallen schrijven & lezen:")
    demo_write_numbers()
    demo_read_numbers()

    print("\n6) Checken of file bestaat:")
    demo_check_file_exists("demo_text.txt")
    demo_check_file_exists("bestaat_niet.txt")

    print("\n7) try/except rond file open:")
    demo_try_except_open()

    print("\n8) try/except/else/finally:")
    demo_try_except_else_finally()

    print("\n9) Exception object met 'as ex':")
    demo_exception_object()

    print("\n10) Custom exception + raise:")
    demo_raise_custom_exception()

    print("\n11) Binary file voorbeeld:")
    demo_binary_file()

    print("\n12) (Optioneel) Webpagina lezen met urllib.request:")
    # demo_read_webpage()  # commentaar laten als je geen internet hebt / op Dodona zit

    print("\n=== EINDE DEMO ===")


if __name__ == "__main__":
    main()
