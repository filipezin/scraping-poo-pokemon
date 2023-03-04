import time, os, sys, random, pandas as pd
from Treinador import Treinador

class Batalha:
    
    def __init__(self, pokemon1, pokemon2):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
        self.str_to_int()

        
        print(self.pokemon1.ataque)
        print(type(self.pokemon1.ataque))
    

    
    def str_to_int(self):
        self.pokemon1.ataque = int(self.pokemon1.ataque)
        self.pokemon1.vida = int(self.pokemon1.vida)
        self.pokemon1.defesa = int(self.pokemon1.defesa)

        self.pokemon2.ataque = int(self.pokemon2.ataque)
        self.pokemon2.vida = int(self.pokemon2.vida)
        self.pokemon2.defesa = int(self.pokemon2.defesa)



    def combate(self):
        os.system('cls')
        self.pokemon1.vida *= 2
        self.pokemon2.vida *= 2

        turno_atual = 1

        if self.pokemon1.velocidade > self.pokemon2.velocidade:
            while True:
                print(f'TURNO ATUAL : {turno_atual}\n{self.pokemon1.nome} ataca!\n')
                turno_atual += 1

                self.animacao()
                hit1, hit2 = self.hits()                
                

                # POKEMON 1 VAI PRIMEIRO
                self.pokemon2.vida -= hit1

                print(f'{self.pokemon1.nome} causou {hit1} de dano!!\n{self.pokemon2.nome} ficou com {self.pokemon2.vida} de HP!', end='\n\n\n')
                time.sleep(2)
                
                if self.pokemon2.vida < 1:
                    print(f'{self.pokemon2.nome} desmaiou!!\n\n{self.pokemon1.nome} é o(a) vencedor(a)!')
                    return self.pokemon1.nome
                # FIM DO TURNO POKEMON 1

                print(f'É a vez do(a) {self.pokemon2.nome} atacar!\n')
                self.animacao()
                # TURNO POKEMON 2
                self.pokemon1.vida -= hit2
                print(f'{self.pokemon2.nome} causou {hit2} de dano!!\n{self.pokemon1.nome} ficou com {self.pokemon1.vida} de HP!',end='\n\n\n')
                time.sleep(2)

                
                if self.pokemon1.vida < 1:
                    print(f'{self.pokemon1.nome} desmaiou!!\n\n{self.pokemon2.nome} é o(a) vencedor(a)!')
                    return self.pokemon2.nome
                # FIM DO TURNO POKEMON 2
        else:
            while True:
                print(f'TURNO ATUAL : {turno_atual}\n{self.pokemon1.nome} ataca!\n')
                turno_atual += 1

                self.animacao()
                hit1, hit2 = self.hits()


                # POKEMON 2 VAI PRIMEIRO
                self.pokemon1.vida -= hit2

                print(f'{self.pokemon2.nome} causou {hit2} de dano!!\n{self.pokemon1.nome} ficou com {self.pokemon1.vida} de HP!', end='\n\n\n')
                time.sleep(2)

                if self.pokemon1.vida < 1:
                    print(f'{self.pokemon1.nome} desmaiou!!\n\n{self.pokemon2.nome} é o(a) vencedor(a)!')
                    return self.pokemon2.nome
                # FIM DO TURNO POKEMON 2

                print(f'É a vez do(a) {self.pokemon1.nome} atacar!\n')
                self.animacao()
                # TURNO POKEMON 1
                self.pokemon2.vida -= hit1
                print(f'{self.pokemon1.nome} causou {hit1} de dano!!\n{self.pokemon1.nome} ficou com {self.pokemon1.vida} de HP!', end='\n\n\n')
                time.sleep(2)

                if self.pokemon2.vida < 1:
                    print(f'{self.pokemon2.nome} desmaiou!!\n\n{self.pokemon1.nome} é o(a) vencedor(a)!')
                    return self.pokemon1.nome
                # FIM DO TURNO POKEMON 1
        


    def animacao(self):
        anim = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(anim)):
            time.sleep(0.10)
            sys.stdout.write('\r' + anim[i % len(anim)])
            sys.stdout.flush()
        print()



    def hits(self):
        return int(self.pokemon1.ataque * (random.randint(80,101)/100) - self.pokemon2.defesa/2) + 10, int(self.pokemon2.ataque * (random.randint(80,101)/100) - self.pokemon1.defesa/2) + 10
        
        
    
## */----------------------------------------------------------------------\* ##



    @property
    def pokemon1(self):
        return self.__pokemon1
    
    @property
    def pokemon2(self):
        return self.__pokemon2



## */----------------------------------------------------------------------\* ##



# t1 = Treinador('Filipe', 'Masculino', 30)
# t1.escolhe_time_aleatorio()

# t2 = Treinador('Isabella', 'Feminino', 25)
# t2.escolhe_time_aleatorio()

# for i in t1.time.keys():
#     t1.time[i].velocidade = 100
#     escolha1 = t1.time[i]
#     break

# for i in t2.time.keys():
#     t2.time[i].velocidade = 50
#     escolha2 = t2.time[i]
#     break



# treta = Batalha(escolha1,escolha2)
# treta.combate()
