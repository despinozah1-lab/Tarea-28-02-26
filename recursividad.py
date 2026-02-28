# ==============================
# FUNCIONES RECURSIVAS
# ==============================


# 1 Convertir a Binario
def convertir_a_binario(numero):
    if numero < 0:
        return "-" + convertir_a_binario(-numero)
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)


# 2 Contar Digitos
def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)


# 3 Raiz Cuadrada Entera
def calcular_raiz_cuadrada(numero, candidato):
    if candidato * candidato > numero:
        return candidato - 1
    return calcular_raiz_cuadrada(numero, candidato + 1)


def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No existe raiz cuadrada real para numeros negativos"
    return calcular_raiz_cuadrada(numero, 0)


# 4 Convertir de Romano a Decimal
def convertir_a_decimal(romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])


# 5 Suma de Numeros Enteros
def suma_numeros_enteros(numero):
    if numero <= 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)


# ==============================
# MENU INTERACTIVO (CLI)
# ==============================


def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Convertir a Binario")
    print("2. Contar Digitos")
    print("3. Raiz Cuadrada Entera")
    print("4. Convertir a Decimal desde Romano")
    print("5. Suma de Numeros Enteros")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            numero = int(input("Ingrese un numero entero: "))
            print("Binario:", convertir_a_binario(numero))

        elif opcion == "2":
            numero = int(input("Ingrese un numero entero: "))
            print("Cantidad de digitos:", contar_digitos(numero))

        elif opcion == "3":
            numero = int(input("Ingrese un numero entero: "))
            print("Raiz cuadrada entera:", raiz_cuadrada_entera(numero))

        elif opcion == "4":
            romano = input("Ingrese un numero romano: ").upper()
            print("Equivalente decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            numero = int(input("Ingrese un numero entero positivo: "))
            print("Suma total:", suma_numeros_enteros(numero))

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida, intente nuevamente.")


# Ejecutar programa
if __name__ == "__main__":
    main()
