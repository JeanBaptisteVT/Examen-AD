def combisom(lijst, x):
    for i in range(len(lijst)):
        for j in range(i+1,len(lijst)):
            if lijst[i] + lijst[j] == x:
                return True
    return False

print(combisom([1, 2, 3, 4, 5, 6], 10))