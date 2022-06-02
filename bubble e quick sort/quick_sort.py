import time


def partition(array, low, high):
    i = (low - 1)
    x = array[high]

    for j in range(low, high):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


# low  --> Starting index,
# high  --> Ending index
def I_QuickSort(array, low, high):
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        p = partition(array, low, high)

        # push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


def quickS(f):
    words_with_numbers = []
    words = f.read().split(' ')
    for w in words:
        if any(c.isdigit() for c in w):
            words_with_numbers.append(int(w))
    f.close()
    vet = words_with_numbers
    start = time.time()
    I_QuickSort(vet, 0, len(vet) - 1)
    end = time.time()
    print('\n\n------- Inicio do Vetor Ordenado -------\n\n')
    print(vet)
    print(f"\nQuick Sort demorou: {end - start} segundos")
    print('\n\n------- Fim do Vetor Ordenado -------\n\n')



