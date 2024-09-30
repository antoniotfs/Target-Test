texto = input("Digite uma string: ")
quantidade = texto.lower().count('a')
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes.")
else:
    print("A letra 'a' não aparece na string.")