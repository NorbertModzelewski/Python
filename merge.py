def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        lewa = lista[:mid]
        prawa = lista[mid:]

        mergeSort(lewa)
        mergeSort(prawa)

        i = 0
        j = 0

        k = 0

        while i < len(lewa) and j < len(prawa):
            if lewa[i] <= prawa[j]:

                lista[k] = lewa[i]

                i += 1
            else:
                lista[k] = prawa[j]
                j += 1

            k += 1

        while i < len(lewa):
            lista[k] = lewa[i]
            i += 1
            k += 1

        while j < len(prawa):
            lista[k] = prawa[j]
            j += 1
            k += 1

lista = [69, 2137, 93, 13, 77, 31, 44, 5, 20]
mergeSort(lista)
print(lista)