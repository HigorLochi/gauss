from asyncio.windows_events import NULL
from tracemalloc import stop

from app.math.GaussElimination import GaussElimination
from app.handlers.SystemInputHandler import SystemInputHandler
from app.utils.SystemPrinter import SystemPrinter

def main():
    dimensions = SystemInputHandler.getSystemDimensions()
    
    system = [ [0] * dimensions["columns"] for i in range(dimensions["rows"])]

    system = SystemInputHandler.getSystemValues(system)

    gaussElimination = GaussElimination(system);

    SystemPrinter.print(system);

    valoresfinais = gaussElimination.solve()

    SystemPrinter.printFinalValues(valoresfinais);

main()