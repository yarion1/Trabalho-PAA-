from quick_sort import quickS


def quick():
    sair = 1
    while sair != 0:
        op = input("\nDigite a opcao desejada:\n1-Desordenado\n2-Crescente\n3-Decrescente\n0-Sair\nResposta: ")
        op = int(op)
        sair = op

        if op == 1:
            quickDes()
        elif op == 2:
            quickDec()
        elif op == 3:
            quickCres()
        elif op == 0:
            print("Voltando ao menu....\n")
        else:
            print("Entrada inválida")


def quickDes():
    sair = 1
    while sair != 0:
        op = input("\nDigite a opcao desejada:\n1-100\n2-1.000\n3-10.000\n4-20.000\n5-50.000\n6-100.000\n7-500.000\n8"
                   "-1.000.000\n0-Sair\nResposta: ")
        op = int(op)
        sair = op

        if op == 1:
            f = open("./numeros/Desordenado/cem.txt", "r")
            quickS(f)
        elif op == 2:
            f = open("./numeros/Desordenado/mil.txt", "r")
            quickS(f)
        elif op == 3:
            f = open("./numeros/Desordenado/dezMil.txt", "r")
            quickS(f)
        elif op == 4:
            f = open("./numeros/Desordenado/vinteMil.txt", "r")
            quickS(f)
        elif op == 5:
            f = open("./numeros/Desordenado/cinquentaMil.txt", "r")
            quickS(f)
        elif op == 6:
            f = open("./numeros/Desordenado/cemMil.txt", "r")
            quickS(f)
        elif op == 7:
            f = open("./numeros/Desordenado/quinhentosMil.txt", "r")
            quickS(f)
        elif op == 8:
            f = open("./numeros/Desordenado/umMilhao.txt", "r")
            quickS(f)
        elif op == 0:
            print("Voltando ao menu....\n")
        else:
            print("Entrada inválida")


def quickDec():
    sair = 1
    while sair != 0:
        op = input("\nDigite a opcao desejada:\n1-100\n2-1.000\n3-10.000\n4-20.000\n5-50.000\n6-100.000\n7-500.000\n8"
                   "-1.000.000\n0-Sair\nResposta: ")
        op = int(op)
        sair = op

        if op == 1:
            f = open("./numeros/Decrescente/cem.txt", "r")
            quickS(f)
        elif op == 2:
            f = open("./numeros/Decrescente/mil.txt", "r")
            quickS(f)
        elif op == 3:
            f = open("./numeros/Decrescente/dezMil.txt", "r")
            quickS(f)
        elif op == 4:
            f = open("./numeros/Decrescente/vinteMil.txt", "r")
            quickS(f)
        elif op == 5:
            f = open("./numeros/Decrescente/cinquentaMil.txt", "r")
            quickS(f)
        elif op == 6:
            f = open("./numeros/Decrescente/cemMil.txt", "r")
            quickS(f)
        elif op == 7:
            f = open("./numeros/Decrescente/quinhentosMil.txt", "r")
            quickS(f)
        elif op == 8:
            f = open("./numeros/Decrescente/umMilhao.txt", "r")
            quickS(f)
        elif op == 0:
            print("Voltando ao menu....\n")
        else:
            print("Entrada inválida")


def quickCres():
    sair = 1
    while sair != 0:
        op = input("\nDigite a opcao desejada:\n1-100\n2-1.000\n3-10.000\n4-20.000\n5-50.000\n6-100.000\n7-500.000\n8"
                   "-1.000.000\n0-Sair\nResposta: ")
        op = int(op)
        sair = op

        if op == 1:
            f = open("./numeros/Crescente/cem.txt", "r")
            quickS(f)
        elif op == 2:
            f = open("./numeros/Crescente/mil.txt", "r")
            quickS(f)
        elif op == 3:
            f = open("./numeros/Crescente/dezMil.txt", "r")
            quickS(f)
        elif op == 4:
            f = open("./numeros/Crescente/vinteMil.txt", "r")
            quickS(f)
        elif op == 5:
            f = open("./numeros/Crescente/cinquentaMil.txt", "r")
            quickS(f)
        elif op == 6:
            f = open("./numeros/Crescente/cemMil.txt", "r")
            quickS(f)
        elif op == 7:
            f = open("./numeros/Crescente/quinhentosMil.txt", "r")
            quickS(f)
        elif op == 8:
            f = open("./numeros/Crescente/umMilhao.txt", "r")
            quickS(f)
        elif op == 0:
            print("Voltando ao menu....\n")
        else:
            print("Entrada inválida")
