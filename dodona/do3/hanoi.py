def hanoi(n):
    def verplaats(n, van, naar, hulp):
        # geeft aantal stappen terug
        if n == 1:
            print(f"Schijf 1 van {van} naar {naar}")
            return 1
        else:
            stappen = 0
            # 1) n-1 schijven van van -> hulp
            stappen += verplaats(n - 1, van, hulp, naar)
            # 2) grootste schijf n van van -> naar
            print(f"Schijf {n} van {van} naar {naar}")
            stappen += 1
            # 3) n-1 schijven van hulp -> naar
            stappen += verplaats(n - 1, hulp, naar, van)
            return stappen

    totaal = verplaats(n, "A", "C", "B")
    print(f"{totaal} stappen gedaan")
