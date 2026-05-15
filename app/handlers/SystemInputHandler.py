from app.variables.systemMaximumLength import maximumLength

class SystemInputHandler:
    def getSystemDimensions():
        while True:
            print("What will be the dimension? (maximum = " + str(maximumLength) + ")")
            rows = int(input())
            columns = rows

            if columns + rows <= maximumLength:
                print("Accepted.")
                break
            else:
                print("Not accepted.")

        return {"rows": rows, "columns": columns + 1};

    def getSystemValues(system):
        for i in range(len(system)):
            print("=== System " + str(i + 1) + " ===")

            for j in range(len(system[i])):
                if j < len(system[i]) - 1:
                    print("Input the value of element #" + str(j + 1))
                else:
                    print("Input the value of row #" + str(i + 1))

                system[i][j] = int(input())
        
        return system;
    