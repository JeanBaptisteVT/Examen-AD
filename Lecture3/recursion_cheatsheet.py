
# ---------------------------------------------------------
# 1. WAT IS RECURSIE?
# ---------------------------------------------------------
# Recursie = een functie die zichzelf oproept.
# Een recursieve functie heeft ALTIJD:
#   ✔ een base case (stopvoorwaarde)
#   ✔ een recursive case (oproep naar zichzelf met kleiner probleem)
#
# Belangrijk:
# - Elke call krijgt eigen ruimte op de call stack
# - Recursie stopt pas wanneer de base case bereikt is
# ---------------------------------------------------------


# ---------------------------------------------------------
# 2. FACTORIAL (n!)
# ---------------------------------------------------------
# Definitie:
#   factorial(0) = 1
#   factorial(n) = n * factorial(n-1)
# ---------------------------------------------------------

def factorial(n):
    """Recursieve factorial: n! = n * (n-1)!"""
    if n == 0:            # base case
        return 1
    else:                 # recursive case
        return n * factorial(n - 1)


# ---------------------------------------------------------
# 3. STACK TRACE VOOR FACTORIAL (uit slides)
# ---------------------------------------------------------
# Om te tonen hoe de stack groeit en krimpt.
# ---------------------------------------------------------

def traced_factorial(n, depth=0):
    print("  " * depth + f"Entering factorial({n})")

    if n == 0:
        print("  " * depth + "Returning 1 (base case)")
        return 1

    result = n * traced_factorial(n - 1, depth + 1)

    print("  " * depth + f"Returning {result}")
    return result


# ---------------------------------------------------------
# 4. FIBONACCI (klassieke recursie)
# ---------------------------------------------------------
# Fibonacci:
#   fib(0) = 0
#   fib(1) = 1
#   fib(n) = fib(n-1) + fib(n-2)
# Let op: EXPONENTIËLE tijdcomplexiteit.
# ---------------------------------------------------------

def fib(n):
    if n == 0:        # base case 1
        return 0
    elif n == 1:      # base case 2
        return 1
    else:             # recursive case
        return fib(n - 1) + fib(n - 2)


# ---------------------------------------------------------
# 5. SIMPELE RECURSIE — PRINT n KEER EEN BOODSCHAP
# (Uit slides: nPrintln)
# ---------------------------------------------------------

def nPrintln(message, times):
    if times >= 1:
        print(message)
        nPrintln(message, times - 1)
        # base case: times == 0 → stopt automatisch


# ---------------------------------------------------------
# 6. RECURSIVE PALINDROME (basisversie)
# ---------------------------------------------------------

def isPalindrome(s):
    # base cases: string is leeg of 1 karakter → altijd palindrome
    if len(s) <= 1:
        return True

    # als eerste en laatste karakter verschillen → geen palindrome
    if s[0] != s[-1]:
        return False

    # recursive case: check binnenste substring
    return isPalindrome(s[1:-1])


# ---------------------------------------------------------
# 7. PALINDROME MET HELPER (efficiënter)
# ---------------------------------------------------------

def isPalindrome_helper_version(s):
    return palindromeHelper(s, 0, len(s) - 1)


def palindromeHelper(s, low, high):
    # base case: indices zijn gekruist
    if high <= low:
        return True
    # karakters verschillen → geen palindrome
    if s[low] != s[high]:
        return False

    # recursive case: binnenste gedeelte checken
    return palindromeHelper(s, low + 1, high - 1)


# ---------------------------------------------------------
# 8. RECURSIVE SELECTION SORT (van de slides)
# ---------------------------------------------------------

def recursive_selection_sort(lst, index=0):
    """Sorteert de lijst door het kleinste element vanaf index te vinden en vooraan te plaatsen."""
    if index >= len(lst) - 1:
        return  # base case

    # kleinste element vanaf index
    min_index = index
    for i in range(index + 1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i

    # swap
    lst[index], lst[min_index] = lst[min_index], lst[index]

    # sorteer de rest
    recursive_selection_sort(lst, index + 1)


# ---------------------------------------------------------
# 9. RECURSIVE BINARY SEARCH
# ---------------------------------------------------------

def recursive_binary_search(lst, key, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    # base case: interval leeg → niet gevonden
    if low > high:
        return -1

    mid = (low + high) // 2

    if key == lst[mid]:
        return mid
    elif key < lst[mid]:
        return recursive_binary_search(lst, key, low, mid - 1)
    else:
        return recursive_binary_search(lst, key, mid + 1, high)


# ---------------------------------------------------------
# 10. DIRECTORY SIZE (uit slides)
# ---------------------------------------------------------
# Recursieve benadering:
#   grootte = som van:
#       - bestanden in directory
#       - grootte van alle subdirectories
# ---------------------------------------------------------

import os

def getDirectorySize(path):
    """Geef totale grootte van directory (met subdirs)."""
    total = 0

    for file in os.listdir(path):
        fullpath = os.path.join(path, file)

        if os.path.isfile(fullpath):
            total += os.path.getsize(fullpath)
        else:
            # recursive call voor subdirectory
            total += getDirectorySize(fullpath)

    return total


# ---------------------------------------------------------
# 11. TOWERS OF HANOI (van slides)
# ---------------------------------------------------------
# Idee:
#   Move n disks from A → B using C as buffer.
# ---------------------------------------------------------

def hanoi(n, from_tower, to_tower, aux_tower):
    """Print stappen om n schijven te verplaatsen."""
    if n == 1:
        print(f"Move disk 1 from {from_tower} to {to_tower}")
    else:
        # move n-1 disks naar auxiliary
        hanoi(n - 1, from_tower, aux_tower, to_tower)

        # move biggest disk naar doel
        print(f"Move disk {n} from {from_tower} to {to_tower}")

        # move n-1 disks van auxiliary naar doel
        hanoi(n - 1, aux_tower, to_tower, from_tower)


# ---------------------------------------------------------
# 12. RECURSION VS ITERATION (voorbeeld)
# ---------------------------------------------------------

def factorial_iterative(n):
    """Iteratieve versie van factorial om verschil te tonen."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---------------------------------------------------------
# 13. TAIL RECURSION (van slides)
# ---------------------------------------------------------
# Tail recursion: GEEN verdere operaties na de recursive call.
#
# Python ondersteunt GEEN tail recursion optimization,
# maar dit is hoe het concept eruitziet.
# ---------------------------------------------------------

def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator   # alles is opgespaard in accumulator (tail recursive)
    else:
        # recursive call is de allerlaatste operatie
        return factorial_tail(n - 1, accumulator * n)


# ---------------------------------------------------------
# main() om voorbeelden te tonen (optioneel)
# ---------------------------------------------------------

def main():
    print("=== FACTORIAL ===")
    print("factorial(5) =", factorial(5))

    print("\n=== TRACED FACTORIAL ===")
    traced_factorial(4)

    print("\n=== FIBONACCI ===")
    print("fib(6) =", fib(6))

    print("\n=== PALINDROME ===")
    print("racecar ?", isPalindrome("racecar"))
    print("hello ?", isPalindrome("hello"))

    print("\n=== PALINDROME HELPER ===")
    print("abba ?", isPalindrome_helper_version("abba"))

    print("\n=== RECURSIVE SELECTION SORT ===")
    lst = [5, 3, 7, 1, 4]
    recursive_selection_sort(lst)
    print(lst)

    print("\n=== RECURSIVE BINARY SEARCH ===")
    print(recursive_binary_search([1, 3, 5, 7, 9], 7))

    print("\n=== HANOI ===")
    hanoi(3, "A", "B", "C")

    print("\n=== TAIL RECURSION (conceptueel) ===")
    print("factorial_tail(5) =", factorial_tail(5))

    print("\n=== EINDE DEMO CHAPTER 15 ===")


if __name__ == "__main__":
    main()
