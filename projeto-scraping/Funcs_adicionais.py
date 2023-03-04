from Treinador import Treinador
from Load import loader
from time import sleep
from sys import stdout
import os



def delay_print(string):
    for letra in string:
        stdout.write(letra)
        stdout.flush()
        sleep(0.05)

def intro():
    os.system('cls')
    delay_print('Nome: Filipe Albanes Nobre Santos\nTurma: 2TDSPI\nRM: 94377\nLista de exercícios 1\n')
    sleep(2)
    loader('Inicializando programa...', 'OK!')


def cadastro():
    os.system('cls')
    # loader('Iniciando procedimento de cadastro de treinadores... ', 'OK!') REINICIAR
    cad = {}
    for i in range(1,3):
        print(f'TREINADOR {i}')
        treinador = Treinador(input(f'Nome do(a) treinador(a) {i}  =>  '), input(f'Sexo do(a) treinador(a) {i}  =>  '), input(f'Idade do(a) treinador(a) {i}  =>  '))
        cad[treinador.nome] = treinador
        print()
    return cad, list([i for i in cad.keys()])


def escolhe_time(treinador):
    if input('[A]leatório ou [M]anualmente? (A/M)\n=>  ').upper() == 'A':
        os.system('cls')
        return treinador.escolhe_time_aleatorio()
    os.system('cls')
    return treinador.escolhe_time_manualmente()



    
        
