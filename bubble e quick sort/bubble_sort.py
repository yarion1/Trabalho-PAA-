import time


# Bubble sort in Python
def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp




def bubbleS(f):
    words_with_numbers = []
    words = f.read().split(' ')
    for w in words:
        if any(c.isdigit() for c in w):
            words_with_numbers.append(int(w))
    f.close()
    vet = words_with_numbers
    start = time.time()
    bubbleSort(vet)
    end = time.time()
    print('\n\n------- Inicio do Vetor Ordenado -------\n\n')
    # print(vet)
    print(f"\nBubble Sort demorou: {end - start} segundos")
    print('\n\n------- Fim do Vetor Ordenado -------\n\n')
