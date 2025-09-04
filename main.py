from Clases.avanzadas import Operaciones

def main():
    op = Operaciones()
    print("\n--- Calculadora ---")
    print("1. Potencia")
    print("2. Raíz n-ésima")

    opcion = input("Elige una opción: ")

    op.leerNumeros()

    if opcion == "1":
        op.potencia()
    elif opcion == "2":
        op.raiz()
    else:
        print("Opción no válida")
        return

    op.mostrarResultado()


if __name__ == "__main__":
    main()