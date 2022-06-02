from bubble_esc import bubble
from quick_esc import quick

if __name__ == "__main__":
    sair = 1
    while sair != 0:
        op = input("Digite a opcao desejada:\n1-Bubble Sort\n2-Quick Sort\n0-Sair\nResposta: ")
        op = int(op)
        sair = op

        if op == 1:
            bubble()
        elif op == 2:
            quick()
        elif op == 0:
            print("Voltando ao menu....\n")
        else:
            print("Entrada inválida")