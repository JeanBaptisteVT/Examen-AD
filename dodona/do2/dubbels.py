def dubbel(lijst):
    for i in lijst:
        if lijst.count(i) == 2:
            return i




def dubbels(lijst):
    lijst_eenmaal = set()
    lijst_meermaal = set()
    for i in lijst:
        if lijst.count(i) == 1:
            lijst_eenmaal.add(i)
        else:
            lijst_meermaal.add(i)

    return lijst_eenmaal, lijst_meermaal

print(dubbels([1, 2, 3, 4, 2]))


