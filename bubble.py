liczby = [10, 3, 7, 8, 1, 6, 2, 9, 4, 5, 0]

def sort(liczby):
    for i in range(len(liczby) - 1, 0, -1):
        for j in range(i):
            if liczby[j] > liczby[j + 1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]

sort(liczby)
print(liczby)