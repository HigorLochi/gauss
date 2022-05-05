from asyncio.windows_events import NULL
from tracemalloc import stop

#globals
letras = ["X","A","B","C","E","F","G","H","I","J","K"]

def verifyValues(valores,letra):
    if not valores:
        return False
    for valor in valores:
        if valor[0] == letra:
            return True

    return False

def inputValues():
    linhas = 0
    colunas = 0
    response = NULL

    while True:
        print("Qual será a dimensão do sistema? (maximo = 10)")
        colunas = int(input())
        linhas = colunas

        if colunas <= 10 and linhas <= 10:
            colunas = colunas+1
            print("Valores aceitos.")
            response = [ [0]*colunas for i in range(linhas)]
            break
        else:
            print("Valores não aceitos.")

    for i in range(linhas):
        print("=== Sistema "+str(i+1)+" ===")
        for j in range(colunas):
            if j < colunas-1:
                print("Insira o "+str(j+1)+"º elemento: ")
            else:
                print("Insira o valor da linha "+str(i)+": ")

            response[i][j] = int(input())

    return response

def main():
    sistema = inputValues()
    pivoIteracao = 1

    #formatação do sistema
    for linha in range(len(sistema)):
        if(linha == 0):
                continue
        for aux in range(pivoIteracao):
            pivo = sistema[pivoIteracao][aux]/sistema[aux][aux]
            for coluna in range(len(sistema[linha])):
                sistema[linha][coluna] = sistema[linha][coluna]-(sistema[linha-pivoIteracao+aux][coluna]*pivo)
                if -0.00001 <= sistema[linha][coluna] <= 0.00001:
                    sistema[linha][coluna] = 0
        pivoIteracao = pivoIteracao+1

    #separar valores
    valoresfinais = []
    valoriteracao = 1

    print("Sistema: ")
    for linha in (sistema):
        print(linha)
    print()

    for linha in range(len(sistema)):
        valorlinha = sistema[len(sistema)-valoriteracao][len(sistema[linha])-1]
        divisor = sistema[len(sistema)-valoriteracao][len(sistema[linha])-valoriteracao-1]

        for coluna in range(len(sistema[linha])):
            if(coluna == 0):
                continue
            if coluna != valoriteracao:
                subtraente = sistema[len(sistema)-valoriteracao][len(sistema[linha])-coluna-1]
                for valor in valoresfinais:
                    if coluna == valor[0]:
                        subtraente = subtraente * valor[1]
                valorlinha = valorlinha - subtraente
            else:
                break

        valorfinal = valorlinha/divisor
        if valorfinal == -0:
            valorfinal = 0

        valoresfinais.insert(len(valoresfinais),[coluna,valorfinal])
        valoriteracao = valoriteracao + 1

    for valor in valoresfinais:
        print(str(letras[valor[0]]) + " = " + str(valor[1]))

main()