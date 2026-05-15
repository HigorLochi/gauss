class GaussElimination:
    finalValues = []

    def __init__(self, system):
        self.system = system

    def solve(self):
        self.format()
        self.separation()

        return self.finalValues;

    def format(self):
        pivotIteration = 1

        for row in range(len(self.system)):
            if(row == 0):
                    continue
            for aux in range(pivotIteration):
                pivot = self.system[pivotIteration][aux]/self.system[aux][aux]
                for column in range(len(self.system[row])):
                    self.system[row][column] = self.system[row][column]-(self.system[row-pivotIteration+aux][column] * pivot)
                    if -0.00001 <= self.system[row][column] <= 0.00001:
                        self.system[row][column] = 0
            pivotIteration = pivotIteration+1

        return self.system;

    def separation(self):
        iterationValue = 1

        for row in range(len(self.system)):
            rowValue = self.system[len(self.system)-iterationValue][len(self.system[row])-1]
            divisor = self.system[len(self.system)-iterationValue][len(self.system[row])-iterationValue-1]

            for column in range(len(self.system[row])):
                if(column == 0):
                    continue
                if column != iterationValue:
                    subtractingValue = self.system[len(self.system)-iterationValue][len(self.system[row])-column-1]
                    for finalValue in self.finalValues:
                        if column == finalValue[0]:
                            subtractingValue = subtractingValue * finalValue[1]
                    rowValue = rowValue - subtractingValue
                else:
                    break

            finalValue = rowValue/divisor
            if finalValue == -0:
                finalValue = 0

            self.finalValues.insert(len(self.finalValues),[column,finalValue])
            iterationValue = iterationValue + 1

        return self.finalValues;

    