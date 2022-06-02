# Insertion sort in Python
import time

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    
def menu_crescente(op):
        if op== 1:
            f = open("./numeros/numeros/Crescente/cem.txt", "r")
            convert(f)
        if op== 2:
            f = open("./numeros/numeros/Crescente/mil.txt", "r")
            convert(f)
        if op== 3:
            f = open("./numeros/numeros/Crescente/dezMil.txt", "r")
            convert(f)
        if op== 4:
            f = open("./numeros/numeros/Crescente/vinteMil.txt", "r")
            convert(f)
        if op== 5:
            f = open("./numeros/numeros/Crescente/cinquentaMil.txt", "r")
            convert(f)
        if op== 6:
            f = open("./numeros/numeros/Crescente/cemMil.txt", "r")
            convert(f)
        if op== 7:
            f = open("./numeros/numeros/Crescente/quinhentosMil.txt", "r")
            convert(f)
        if op== 8:
            f = open("./numeros/numeros/Crescente/umMilhao.txt", "r")
            convert(f)

def menu_decrescente(op):
        if op== 1:
            f = open("./numeros/numeros/Decrescente/cem.txt", "r")
            convert(f)
        if op== 2:
            f = open("./numeros/numeros/Decrescente/mil.txt", "r")
            convert(f)
        if op== 3:
            f = open("./numeros/numeros/Decrescente/dezMil.txt", "r")
            convert(f)
        if op== 4:
            f = open("./numeros/numeros/Decrescente/vinteMil.txt", "r")
            convert(f)
        if op== 5:
            f = open("./numeros/numeros/Decrescente/cinquentaMil.txt", "r")
            convert(f)
        if op== 6:
            f = open("./numeros/numeros/Decrescente/cemMil.txt", "r")
            convert(f)
        if op== 7:
            f = open("./numeros/numeros/Decrescente/quinhentosMil.txt", "r")
            convert(f)
        if op== 8:
            f = open("./numeros/numeros/Decrescente/umMilhao.txt", "r")
            convert(f)

def menu_desordenado(op):

        if op==1:
            f = open("./numeros/numeros/Desordenado/cem.txt", "r")
            convert(f)
        if op== 2:
            f = open("./numeros/numeros/Desordenado/mil.txt", "r")
            convert(f)
        if op== 3:
            f = open("./numeros/numeros/Desordenado/dezMil.txt", "r")
            convert(f)
        if op== 4:
            f = open("./numeros/numeros/Desordenado/vinteMil.txt", "r")
            convert(f)
        if op== 5:
            f = open("./numeros/numeros/Desordenado/cinquentaMil.txt", "r")
            convert(f)
        if op== 6:
            f = open("./numeros/numeros/Desordenado/cemMil.txt", "r")
            convert(f)
        if op== 7:
            f = open("./numeros/numeros/Desordenado/quinhentosMil.txt", "r")
            convert(f)
        if op== 8:
            f = open("./numeros/numeros/Desordenado/umMilhao.txt", "r")
            convert(f)

def convert(f):
    words_with_numbers = []
    words = f.read().split(" ")
    for w in words:
        if any(c.isdigit() for c in w):
            words_with_numbers.append(int(w))
    f.close()
    data = words_with_numbers
    start = time.time()
    insertionSort(data)
    end = time.time()
    print('Array colocado em ordem:')
    # print(data)
    print("\n")
    print("=/"*50)
    print(f"O programa demorou {end - start} segundos para executar.")
    print("=/"*50)

op = 1
while op!=0:

    op = int(input("Qual tipo de lista deseja processar?\n\n1 - Crescente\n2 - Decrescente\n3 - Desordenado\n0 - Sair\n\n->"))

    optipo = int(input("Qual o tamanho da lista deseja executar?\n\n 1 - Cem\n 2 - Mil\n 3 - Dez Mil\n 4 - Vinte Mil\n 5 - Cinquenta Mil\n 6 - Cem Mil\n 7 - Quinhentos Mil\n 8 - Um Milhão\n\n->"))

    if op==1:
            print("\nExecutando Crescente...")
            menu_crescente(optipo)
        
    if op==2:
            print("\nExecutando Decrescente...")
            menu_decrescente(optipo)
        
    if op==3:
            print("\nExecutando Aleatório...")
            menu_desordenado(optipo)
    

