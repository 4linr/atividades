#Desenvolva um algoritmo que solicite ao usuário que digite uma string e verifique se a string contém apenas letras maiúsculas. Se a string contiver letras minúsculas, levante uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima uma mensagem informando que a string contém apenas letras maiúsculas.

class Maiscula(Exception):
     pass

try:

    palavra = ((input("Digite palavras com letras maiusculas!")))
    if palavra.isupper():
        print("Certo!")

    else:
        raise Maiscula("Precisa ser maiuscula")
    
except Maiscula as e:
    print(e)


    