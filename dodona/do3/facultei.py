
def faculteit_rec(x):
    if x ==1:
        return 1
    else:
        return x*faculteit_rec(x-1)

aantal_testen = int(input("aantal testen"))
for i in range(aantal_testen):
    getal = int(input("getal"))
    if getal > 13:
        print('number is too big')
        break
    else:
        print(faculteit_rec(getal))

