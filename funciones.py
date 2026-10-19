def menu():
    print("\n-------------------- CAJERO AUTOMATICO --------------------")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    print("-" * 60)

def retirar_saldo(saldo_disponible, minimo):
    while True:
        retirar = int(input("\nIngrese la cantidad de dinero que va a retirar de su saldo: "))
    
        # ERRORES
        if retirar > saldo_disponible: # ERROR 1
            print("\nError, no puedes retirar mas del saldo disponible que tienes.")
        elif retirar < 0: # ERROR 2
            print("\nError, no puedes retirar cantidades negativas.")
        elif retirar < minimo: # EL MINIMO DE RETIRO
            print(f"\nEl minimo de retiro es de ${minimo:,.0f}")
        else:
            saldo_disponible -= retirar
            print(f"\nRetiraste ${retirar:,.0f}")
            break

    return saldo_disponible

def depositar_saldo(saldo_disponible, minimo):
    while True:
        depositar = int(input("\nIngrese la cantidad de dinero que va a depositar a su saldo: "))
    
        # ERRORES
        if depositar < 0: # ERROR 1
            print("\nError, no puedes depositar cantidades negativas.")
        elif depositar < minimo:
            print(f"\nEl minimo de depositar es de ${minimo:,.0f}")
        else:
            saldo_disponible += depositar
            print(f"\nDepositaste ${depositar:,.0f}")
            break

    return saldo_disponible