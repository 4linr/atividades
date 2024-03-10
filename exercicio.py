class Excecao(Exception):
    pass


try:     
    num = int(input("Digite um número"))
    if num %2 == 0:
        print("O número é par!")
    else:
        raise Excecao("O número é ímpar!")
           
except Excecao as e:
    print(e)