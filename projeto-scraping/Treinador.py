import scraping as sc
import random
from Pessoa import Pessoa
import os, sys
import time
import pandas as pd



class Treinador(Pessoa):

    # def __init__(self, nome, sexo, idade):
        
    #     self.time = {}
    def __init__(self, nome, sexo, idade):
        super().__init__(nome, sexo, idade)
        self.time = {}


## */----------------------------------------------------------------------\* ##



    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value



## */----------------------------------------------------------------------\* ##
    def delay_print(self, string):
        for letra in string:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(0.04)


    def mostra_pokemons(self):
        return pd.DataFrame([[i.id,i.nome,i.poder] for i in sc.lista_objetos],
                             columns=['ID','NOME','PODER']).to_string(index=False)
     
    def escolhe_time_aleatorio(self):
        equipe = {i : sc.lista_objetos[random.randint(0,len(sc.lista_objetos)-1)] for i in range(1,7-len(self.time.keys()))}
        equipe = {equipe[i].nome : equipe[i] for i in range(1,len(equipe.keys())+1)}
        self.time = equipe
    


    def escolhe_time_manualmente(self):
        

        if len(self.time.keys()) == 6:
            return f'Você já possui o número máximo de pokemons em seu time.'


        while len(self.time.keys()) < 6:
            print(self.mostra_pokemons(),end='\n\n\n')
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
            self.add_pokemon(id_pokemon)
            if len(self.time.keys()) > 0:
                print('Seus pokemons atuais: \n')
                print(self.meus_pokemons(),end='\n\n')
                time.sleep(2)
                os.system('cls')
            

        
    def add_pokemon(self,id):
        pokemon = sc.lista_objetos[id]

        print(f'Pokemon escolhido: \n')
        print(pokemon)
        
        if input(f'Deseja adicionar {pokemon.nome} para o seu time? S/N\n=> ').upper() == 'S':
            self.time[pokemon.nome] = pokemon
            print()
        else:
            self.delay_print(f'{pokemon.nome} não foi adicionado ao seu time.\n\n')
            time.sleep(2)
            
            
        


    def remove_pokemon(self):
        for i in list(self.time.keys()).copy():
            os.system('cls')
            print(self.meus_pokemons())
        
            if input(f'\n\nREMOVER {self.time[i].nome}? S para remover ou pressione qualquer tecla para continuar\n\n=>').upper() == 'S':
                del self.time[i]
        os.system('cls')
        print(self.meus_pokemons())        
        
        
        
    def atribs(self,dic,i):
        return [self.time[i].id, self.time[i].nome, self.time[i].poder]



    def meus_pokemons(self):
        df2 = pd.DataFrame([self.atribs(self.time,i) for i in self.time.keys()],columns=['ID', 'Nome', 'Poder'])
        return df2.to_string(index=False)
        
        
        
## */----------------------------------------------------------------------\* ##
        
    

    def __str__(self):
        return f'NOME: {self.nome.upper()}\nSEXO: {self.sexo.upper()}\nIDADE: {self.idade}'

                
            





# t1 = Treinador('Filipe', 'Masculino', 30)
# t1.escolhe_time_aleatorio()
# t1.escolhe_time_manualmente()

# for i in t1.time.keys():
#     print(t1.time[i])