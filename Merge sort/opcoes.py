from allsorts import MergeS


def number_to_string(opc):
    if opc == 0:
        return print("Saindo.....\n")
    elif opc == 1:
        return merge()
    else:
        return print("Entrada inválida")


def merge():
    opc = input("Digite a opcao desejada:\n1-100\n2-1.000\n3-10.000\n4-20.000\n5-50.000\n6-100.000\n7-500.000\n8-1.000.000\nResposta: ")
    opc = int(opc)

    if opc == 1:
        f = open("Desordenado/cem.txt", "r")
        MergeS(f)
        return ()
    elif opc == 2:

        f = open("Desordenado/mil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 3:
        f = open("Desordenado/dezMil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 4:
        f = open("Desordenado/vinteMil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 5:
        f = open("Desordenado/cinquentaMil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 6:
        f = open("Desordenado/cemMil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 7:
        f = open("Desordenado/quinhentosMil.txt", "r")
        MergeS(f)
        return ()
    elif opc == 8:
        f = open("Desordenado/umMilhao.txt", "r")
        MergeS(f)
        return ()
    else:
        return print("Entrada inválida")
