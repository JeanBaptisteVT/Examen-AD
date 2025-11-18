"""
chapter14_tuples_sets_dicts.py

Cheatsheet voor:
- Tuples  (immutable lijsten)
- Sets    (unieke, ongeordende elementen, snelle membership test)
- Dictionaries (key/value mapping)

Gebaseerd op Chapter 14 uit de cursus (Liang / Les 2.pdf).
Alle voorbeelden hebben duidelijke # opmerkingen zodat je ze op examen snel kan begrijpen.
"""

# ---------------------------------------------------------
# 1. TUPLES
# ---------------------------------------------------------
# Tuples lijken op lijsten, maar zijn IMMUTABLE:
# - je kan elementen lezen (indexering, slicing)
# - je kan ze NIET wijzigen (geen append, remove, itemassignment)
#
# Gebruik een tuple wanneer:
# - de data niet mag/mag veranderen
# - je structuur efficiënter wil dan een list
# ---------------------------------------------------------


def demo_tuples():
    # Lege tuple
    t1 = ()   # tuple zonder elementen

    # Tuple met drie elementen
    t2 = (1, 3, 5)

    # Tuple maken vanuit een list-comprehension
    t3 = tuple([2 * x for x in range(1, 5)])  # (2, 4, 6, 8)

    # Tuple maken vanuit een string → tuple van karakters
    t4 = tuple("abac")  # ('a', 'b', 'a', 'c')

    print("t1 =", t1)
    print("t2 =", t2)
    print("t3 =", t3)
    print("t4 =", t4)

    # Tuples ondersteunen indexering en slicing zoals lists
    print("t2[0] =", t2[0])        # 1
    print("t2[1:3] =", t2[1:3])    # (3, 5)

    # t2[0] = 99  # DIT GEEFT EEN FOUT: 'tuple' object does not support item assignment
    # → dit toont dat tuples immutable zijn


# ---------------------------------------------------------
# 2. SETS
# ---------------------------------------------------------
# Sets:
# - collectie van unieke elementen
# - geen volgorde (unordered)
# - snelle "in"-check: x in s
#
# Goede keuze als:
# - je GEEN dubbele elementen wil
# - volgorde niet belangrijk is
# - je vaak membership wil testen (zoals No Fly List)
# ---------------------------------------------------------


def demo_sets_basic():
    # Lege set
    s1 = set()

    # Set met drie elementen
    s2 = {1, 3, 5}

    # Set maken vanuit een list of tuple
    s3 = set([1, 3, 5])  # zelfde als s2

    # Set met comprehension
    s4 = set([x * 2 for x in range(1, 6)])  # {2, 4, 6, 8, 10}

    # Set maken vanuit string → unieke letters
    s5 = set("abac")  # {'a', 'b', 'c'}

    print("s1 =", s1)
    print("s2 =", s2)
    print("s3 =", s3)
    print("s4 =", s4)
    print("s5 =", s5)

    # Elementen toevoegen en verwijderen
    s1 = {1, 2, 4}
    s1.add(6)          # {1, 2, 4, 6}
    print("na add(6):", s1)

    # Basisfuncties
    print("len(s1) =", len(s1))
    print("max(s1) =", max(s1))
    print("min(s1) =", min(s1))
    print("sum(s1) =", sum(s1))

    # Membership test
    print("3 in s1? ->", 3 in s1)
    print("2 in s1? ->", 2 in s1)

    # Element verwijderen
    s1.remove(4)       # {1, 2, 6}
    print("na remove(4):", s1)


def demo_sets_relations_and_ops():
    s1 = {1, 2, 4}
    s2 = {1, 2, 4, 5, 6}

    # Subset / Superset
    print("s1 =", s1)
    print("s2 =", s2)
    print("s1.issubset(s2)? ->", s1.issubset(s2))      # True
    print("s2.issuperset(s1)? ->", s2.issuperset(s1))  # True

    # Vergelijkingsoperatoren hebben speciale betekenis:
    # s1 < s2  → s1 is een PROPER subset van s2
    # s1 <= s2 → s1 is subset van s2 (mag gelijk zijn)
    print("s1 < s2?  ->", s1 < s2)   # True (proper subset)
    print("s2 > s1?  ->", s2 > s1)   # True (proper superset)

    # Sets negeren volgorde: {1,2,4} == {2,1,4}
    print("{1,2,4} == {2,1,4}? ->", {1, 2, 4} == {2, 1, 4})

    # Set operations:
    a = {1, 2, 4}
    b = {1, 3, 5}

    # UNION
    print("a | b =", a | b)                # {1, 2, 3, 4, 5}
    print("a.union(b) =", a.union(b))

    # INTERSECTION
    print("a & b =", a & b)                # {1}
    print("a.intersection(b) =", a.intersection(b))

    # DIFFERENCE
    print("a - b =", a - b)                # {2, 4}
    print("a.difference(b) =", a.difference(b))

    # SYMMETRIC DIFFERENCE (elementen die in precies één van beide sets zitten)
    print("a ^ b =", a ^ b)                # {2, 3, 4, 5}
    print("a.symmetric_difference(b) =", a.symmetric_difference(b))


def demo_set_no_fly_example():
    # Simpel voorbeeld uit slides: No Fly List
    no_fly_list = {"Alice", "Bob", "Charlie"}  # unieke namen, volgorde onbelangrijk

    name = "Bob"
    if name in no_fly_list:
        print(name, "mag NIET vliegen (staat in de no-fly list).")
    else:
        print(name, "mag vliegen.")


# ---------------------------------------------------------
# 3. DICTIONARIES
# ---------------------------------------------------------
# Dictionary:
# - collectie van key/value-paren
# - toegang tot value via key (niet via index)
# - keys zijn uniek, values mogen gelijk zijn
# - enorm efficiënt voor lookups (zoals studentID → studentdata)
#
# Syntax:
#   d = {}
#   d = {"john": 40, "peter": 45}
# ---------------------------------------------------------


def demo_dict_basic():
    # Lege dictionary
    d = {}

    # Dictionary met twee entries
    ages = {"john": 40, "peter": 45}

    print("ages =", ages)

    # Entry toevoegen of aanpassen:
    ages["susan"] = 50    # nieuwe key
    ages["john"] = 41     # bestaande key → wordt overschreven
    print("na updates:", ages)

    # Entry verwijderen:
    del ages["peter"]
    print("na del ages['peter']:", ages)

    # Lengte en membership:
    print("len(ages) =", len(ages))
    print("'john' in ages? ->", "john" in ages)
    print("'peter' in ages? ->", "peter" in ages)

    # Toegang via key:
    print("ages['john'] =", ages["john"])

    # Itereren over dictionary:
    for key in ages:
        print(key, ":", ages[key])


def demo_dict_methods():
    d = {"john": 40, "peter": 45, "susan": 50}

    print("dictionary =", d)

    # keys(), values(), items() → geven "view-objects" (lijkt op tuples in slides)
    print("keys()   ->", list(d.keys()))      # ['john', 'peter', 'susan']
    print("values() ->", list(d.values()))    # [40, 45, 50]
    print("items()  ->", list(d.items()))     # [('john',40), ('peter',45), ...]

    # get(key) → veiliger dan d[key], want geeft None of default als key niet bestaat
    print("d.get('john') =", d.get("john"))
    print("d.get('anna') =", d.get("anna"))          # None
    print("d.get('anna', -1) =", d.get("anna", -1))  # default -1

    # pop(key) → verwijdert key en geeft value terug
    value = d.pop("peter")
    print("na pop('peter'), value =", value, ", d =", d)

    # popitem() → verwijdert en returnt willekeurig (in practice: laatste) (key, value)
    kv = d.popitem()
    print("na popitem(), kv =", kv, ", d =", d)

    # clear() → maakt dictionary leeg
    d.clear()
    print("na clear(), d =", d)


# ---------------------------------------------------------
# 4. CASE STUDY: COUNT OCCURRENCES OF WORDS (dictionary)
# ---------------------------------------------------------
# Uit slides: CountOccurrenceOfWords
# We tellen hoe vaak elk woord voorkomt in een tekst.
#
# Algoritme:
# - splits de tekst in woorden (bv. via split())
# - per woord:
#       als woord nog niet in dictionary → d[word] = 1
#       anders → d[word] += 1
# ---------------------------------------------------------


def count_word_occurrences_in_text(text):
    # Maak alles lowercase om "The" en "the" als hetzelfde woord te tellen
    text = text.lower()

    # Simpele split op whitespace (voor examen is dit voldoende)
    words = text.split()

    counts = {}  # dictionary: word → aantal keer

    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

    # Resultaten alfabetisch tonen
    for word in sorted(counts.keys()):
        print(word, ":", counts[word])


def count_word_occurrences_in_file(filename):
    """Leest een tekstbestand in en telt het aantal keer dat elk woord voorkomt."""
    try:
        f = open(filename, "r", encoding="utf-8")
        text = f.read()
        f.close()
    except Exception as ex:
        print("Kon bestand niet openen:", ex)
        return

    count_word_occurrences_in_text(text)


# ---------------------------------------------------------
# main: gebruik dit enkel om te testen; op examen mag je enkel stukken gebruiken
# ---------------------------------------------------------

def main():
    print("=== DEMO TUPLES ===")
    demo_tuples()

    print("\n=== DEMO SETS (basic) ===")
    demo_sets_basic()

    print("\n=== DEMO SETS (relations & operations) ===")
    demo_sets_relations_and_ops()

    print("\n=== DEMO SET: no-fly list voorbeeld ===")
    demo_set_no_fly_example()

    print("\n=== DEMO DICTIONARIES (basic) ===")
    demo_dict_basic()

    print("\n=== DEMO DICTIONARY METHODS ===")
    demo_dict_methods()

    print("\n=== DEMO: woordfrequentie in tekst ===")
    sample_text = "This is a test. This test is simple. Simple test, simple text."
    count_word_occurrences_in_text(sample_text)

    print("\n=== EINDE DEMO Chapter 14 ===")


if __name__ == "__main__":
    main()
