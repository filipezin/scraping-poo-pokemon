import time,sys,os

import scraping as sc
import Treinador

class Pokebola():

    def __init__(self,treinador,pokemon):
        self.__treinador = treinador
        self.__pokemon = pokemon

    


    def trocar_pokemon(self):
        if input(f'Deseja devolver {self.pokemon.nome} à natureza? S/N\n=> ').upper() == 'S':
            self.delay_print(f'Pokemon retornado à selva.\n\nHora de escolher um novo pokemon para a pokebola.\n\n')
            print(self.treinador.mostra_pokemons())
            while True: 
                try:
                    id_pokemon = int(input('ID do pokemon para adicionar ao seu time\n=> '))-1
                    print()
                    if 0 <= id_pokemon <= len(sc.lista_objetos):
                        break
                    
                    else:
                        raise ValueError()
                    
                except ValueError as e:
                    print('Entrada inválida')
            
            os.system('cls')
            self.treinador.add_pokemon(id_pokemon)
            self.pokemon = sc.lista_objetos[id_pokemon]
            print(f'{self.pokemon.nome} adicionado(a) com sucesso!!\n\nSeu novo time é: ')
            print(self.treinador.meus_pokemons())


    def delay_print(self, string):
        for letra in string:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.04)
    

    @property
    def treinador(self):
        return self.__treinador

    @treinador.setter
    def treinador(self,value):
        self.__treinador = value
    
    @property
    def pokemon(self):
        return self.__pokemon
    
    @treinador.setter
    def pokemon(self, value):
        self.__pokemon = value

        
