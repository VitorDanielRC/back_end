import time

def fazer_arroz():
    print("Fazendo arroz...")
    time.sleep(3)
    print("Arroz Pronto!")


def fazer_carne():
    print("Fazendo Carne...")
    time.sleep(3)
    print("Carne Pronto!")


def fazer_feijao():
    print("Fazendo Feijão...")
    time.sleep(3)
    print("Feijão Pronto!")


def cozinhar():
    fazer_arroz()
    fazer_carne()
    fazer_feijao()
    print("Almoço pronto")

cozinhar()
    