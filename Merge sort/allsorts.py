import time


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


def MergeS(f):
    words_with_numbers = []
    words = f.read().split(' ')
    for w in words:
        if any(c.isdigit() for c in w):
            words_with_numbers.append(int(w))
    f.close()
    vet = words_with_numbers
    print(vet)
    start = time.time()
    mergeSort(vet)
    end = time.time()

    print('\n\n------- Inicio do Vetor Ordenado -------\n\n')
    print(vet)
    print(f"\nMerge Sort demorou: {end - start} segundos")
    print('\n\n------- Fim do Vetor Ordenado -------\n\n')
