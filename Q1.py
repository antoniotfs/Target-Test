def pertence_a_fibonacci(numero):
    a = 0
    b = 1
    while a <= numero:
        if a == numero:
            return True
        c = a
        a = b
        b = c + b
    return False

numero = int(input("Informe um número: "))
if pertence_a_fibonacci(numero):
    print("O número pertence à sequência de Fibonacci")
else:
    print("O número não pertence à sequência de Fibonacci")