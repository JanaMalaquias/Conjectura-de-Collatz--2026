def collatz(numero):
    if numero <= 0:
        raise ValueError("Informe um número inteiro positivo.")

    sequencia = [numero]
    passos = 0

    while numero != 1:
        if numero % 2 == 0:
            numero //= 2
        else:
            numero = numero * 3 + 1

        sequencia.append(numero)
        passos += 1

    return passos, sequencia


try:
    n = int(input("Digite um número inteiro positivo: "))

    passos, sequencia = collatz(n)

    print("\nSequência:")
    print(" -> ".join(map(str, sequencia)))

    print(f"\nQuantidade de passos: {passos}")

except ValueError as e:
    print(f"Erro: {e}")