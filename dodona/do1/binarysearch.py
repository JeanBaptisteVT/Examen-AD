def zoek(lijst, x):
    lijst.sort()
    low = 0
    high = len(lijst)-1

    while high >= low:
        mid = (low + high)//2
        if x > lijst[mid]:
            low = mid + 1

        elif x == lijst[mid]:
            return mid

        else:
            high = mid - 1

    return None

print(zoek([1, 2, 3, 4, 5], 2))


