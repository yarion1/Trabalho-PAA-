import time

filenames = [""]

def convert(file):
    words_with_numbers = []
    words = file.read().split(" ")
    for w in words:
        if any(c.isdigit() for c in w):
            words_with_numbers.append(int(w))
    file.close()
    data = words_with_numbers
    start = time.time()
    selection_sort(data)
    end = time.time()
    print('Array colocado em ordem:')
    # print(data)
    print("\n")
    print("=/"*50)
    print(f"O programa demorou {end - start} segundos para executar.")
    print("=/"*50)


def selection_sort(array):
    length = len(array)

    for item in range(length):
        minimum = item

        for i in range(item + 1, length):
            if array[i] < array[minimum]:
                minimum = i

        (array[item], array[minimum]) = (array[minimum], array[item])
    return array


if __name__ == '__main__':
    diretorios_ordem= ["Crescente","Decrescente","Desordenado"]
    nomes_tamanho=["cem","mil","dezMil","vinteMil","cinquentaMil","cemMil","quinhentosMil","umMilhao"]
    op = int(input("Qual tipo de lista deseja processar?\n\n1 - Crescente\n2 - Decrescente\n3 - Desordenado\n"))
    optipo = int(input("Qual o tamanho da lista deseja executar?\n\n 1 - Cem\n 2 - Mil\n 3 - Dez Mil\n 4 - Vinte Mil\n 5 - Cinquenta Mil\n 6 - Cem Mil\n 7 - Quinhentos Mil\n 8 - Um Milhão\n\n->"))
    file = open("./numeros/"+str(diretorios_ordem[op-1])+"/"+str(nomes_tamanho[optipo-1])+".txt", "r")
    convert(file)


