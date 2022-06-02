from opcoes import number_to_string
import sys

if __name__ == "__main__":
    sys.setrecursionlimit(11000)
    sair = 1
    while sair!=0:
        op = input("Digite a opcao desejada:\n1-Merge Sort\n0-Sair\nResposta:")
        op = int(op)
        sair = op
        number_to_string(op)