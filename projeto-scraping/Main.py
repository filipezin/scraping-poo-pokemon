import scraping as sc
import pandas as pd
import os
from Pokemon import Pokemon
from Treinador import Treinador
import Funcs_adicionais as fn
import Combate
import Pokebola


with open('exercicios.txt','r',encoding="UTF-8") as ex:
    exercicios = [linha[3:].strip() for linha in ex]



def main():
    ## INTRO ##

    # fn.intro() REINICIAR


    

    ## CADASTRO DE TREINADORES ##
    
    # treinadores, chaves = fn.cadastro()
    
    # t1 = treinadores[chaves[0]]
    # t2 = treinadores[chaves[1]]


    ## APAGAR DEPOIS ##
    t1 = Treinador('Filipe', 'Masculino', 29) # APAGAR
    t2 = Treinador('Isabella', 'Feminino', 25) # APAGAR


    ## ESCOLHA DE POKEMONS ##

    # fn.escolhe_time(t1)
    t1.escolhe_time_aleatorio()
    # print('O time do(a) treinador(a) 1 é:\n')
    # print(t1.meus_pokemons())

    # fn.escolhe_time(t2)
    # t2.escolhe_time_aleatorio()
    # print('O time do(a) treinador(a) 2 é:\n')
    # print(t2.meus_pokemons())

    # os.system('cls')
    # print('MENU DE OPÇÕES\n[1] - Remover Pokemon\n[2] - Adicionar Pokemon\n[3] - Comparar Pokemons entre treinadores')
    

    ### COMBATE
    # treta = Combate.Combate(t1,t2)
    # treta.treta()


    ## POKEBOLA
    bola = Pokebola.Pokebola
    

main()



    




        
