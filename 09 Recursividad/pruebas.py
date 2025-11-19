num = 1234


def suma_dígitos_recursiva(num):
    if num < 10:
        print(num)
        return num
    # Obtengo el ultimo digito
    digito = num % 10
    # Al numero le saco ese ultimo digito
    num = num // 10

    print(digito)
    return digito + suma_dígitos_recursiva(num)


suma = suma_dígitos_recursiva(num)
print(suma)
