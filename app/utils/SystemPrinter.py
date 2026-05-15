from app.variables.systemLetters import systemLetters

class SystemPrinter:
    def print(system):
        print("System: ")

        for linha in (system):
            print(linha)

        print()

    def printFinalValues(valoresfinais):
        for valor in valoresfinais:
            print(str(systemLetters[valor[0]]) + " = " + str(valor[1]))

    