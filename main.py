import os
from funciones import menu, retirar_saldo, depositar_saldo

saldo_disponible = 500000
minimo = 10000

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()

    opcion = input("\nIngrese la opcion que desea ejecutar: ")

    if opcion == "4":
        print("\nSaliendo...")
        break

    if opcion == "1":
        print(f"\nTienes un saldo de ${saldo_disponible:,.0f}")
        input("\nPresiona Enter para continuar...")

    elif opcion == "2":
        saldo_disponible = retirar_saldo(saldo_disponible, minimo)
        input("\nPresiona Enter para continuar...")

    elif opcion == "3":
        saldo_disponible = depositar_saldo(saldo_disponible, minimo)
        input("\nPresiona Enter para continuar...")

    else:
        print("Error, opcion invalida")
        input("\nPresiona Enter para continuar...")