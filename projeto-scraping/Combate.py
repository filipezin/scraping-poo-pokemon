import time, os, sys, random


class Combate():

    def __init__(self, treinador1, treinador2):
        self.t1 = treinador1
        self.t2 = treinador2
    


    def animacao(self):
        anim = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(anim)):
            time.sleep(0.05)
            sys.stdout.write('\r' + anim[i % len(anim)])
            sys.stdout.flush()
        print()


    def str_to_int(self,pokemon1, pokemon2):
        pokemon1.ataque = int(pokemon1.ataque)
        pokemon1.vida = int(pokemon1.vida)
        pokemon1.defesa = int(pokemon1.defesa)
        pokemon1.velocidade = int(pokemon1.velocidade)

        pokemon2.ataque = int(pokemon2.ataque)
        pokemon2.vida = int(pokemon2.vida)
        pokemon2.defesa = int(pokemon2.defesa)
        pokemon2.velocidade = int(pokemon2.velocidade)
        return pokemon1,pokemon2




    def treta(self):
        pks1 = [self.t1.time[pokemon] for pokemon in self.t1.time.keys()]
        pks2 = [self.t2.time[pokemon] for pokemon in self.t2.time.keys()]
        t1, t2 = 0,0
        
        for i in range(6):
            pk1,pk2 = self.str_to_int(pks1[i], pks2[i])

            print(f'LUTA {i+1}\n\n{pk1.nome} vs {pk2.nome}!!\n\n')
            time.sleep(2)
            
            ## BALANCEAMENTO SIMPLES ##
            pk1.vida *= 10
            pk1.ataque += 100

            pk2.vida *= 10
            pk2.ataque += 100
            ############################


            vencedor = self.duelo(pk1,pk2)
            if vencedor == pks1[i].nome:
                t1 += 1
            elif vencedor == pks2[i].nome:
                t2 += 1
            print(f'\n\nPlacar atual:\n{self.t1.nome} => {t1} vitória(s)!!\n{self.t2.nome} => {t2} vitórias(s)!!\n\n')
            time.sleep(2)
            

        return print(f'Treinador {self.t1.nome} é o vencedor!' if t1 > t2 else (f'Treinador {self.t2.nome} é o vencedor!' if t2 > t1 else 'Empate!!'))
            
        
            
            
            
            

    def hits(self,pokemon1,pokemon2):
        return int(pokemon1.ataque * (random.randint(80,101)/100) - pokemon2.defesa/2) + 10, int(pokemon2.ataque * (random.randint(80,101)/100) - pokemon1.defesa/2) + 10


    def duelo(self, pokemon1, pokemon2):
        turno_atual = 0
        if pokemon1.velocidade > pokemon2.velocidade:
            while True:
                turno_atual += 1
                hit1, hit2 = self.hits(pokemon1,pokemon2)                

                
                ## POKEMON 1 VAI PRIMEIRO
                print(f'TURNO ATUAL : {turno_atual}\n{pokemon1.nome} ataca!\n')
                self.animacao()
                
                pokemon2.vida -= hit1

                print(f'{pokemon1.nome} causou {hit1} de dano!!\n{pokemon2.nome} ficou com {pokemon2.vida} de HP!', end='\n\n\n')
                time.sleep(2)
                
                if pokemon2.vida < 1:
                    print(f'{pokemon2.nome} desmaiou!!\n\n{pokemon1.nome} é o(a) vencedor(a)!')
                    return pokemon1.nome
                ############################


                # TURNO POKEMON 2
                print(f'É a vez do(a) {pokemon2.nome} atacar!\n')
                self.animacao()                
                
                pokemon1.vida -= hit2

                print(f'{pokemon2.nome} causou {hit2} de dano!!\n{pokemon1.nome} ficou com {pokemon1.vida} de HP!',end='\n\n\n')
                time.sleep(2)

                if pokemon1.vida < 1:
                    print(f'{pokemon1.nome} desmaiou!!\n\n{pokemon2.nome} é o(a) vencedor(a)!')
                    return pokemon2.nome
                ############################

        else:
            while True:
                turno_atual += 1
                hit1, hit2 = self.hits(pokemon1,pokemon2)


                ## POKEMON 2 VAI PRIMEIRO
                print(f'TURNO ATUAL : {turno_atual}\n{pokemon2.nome} ataca!\n')
                self.animacao()

                pokemon1.vida -= hit2

                print(f'{pokemon2.nome} causou {hit2} de dano!!\n{pokemon1.nome} ficou com {pokemon1.vida} de HP!', end='\n\n\n')
                time.sleep(2)

                if pokemon1.vida < 1:
                    print(f'{pokemon1.nome} desmaiou!!\n\n{pokemon2.nome} é o(a) vencedor(a)!')
                    time.sleep(2)
                    return pokemon2.nome
                ############################


                ## TURNO POKEMON 1
                print(f'É a vez do(a) {pokemon1.nome} atacar!\n')
                self.animacao()

                pokemon2.vida -= hit1

                print(f'{pokemon1.nome} causou {hit1} de dano!!\n{pokemon2.nome} ficou com {pokemon2.vida} de HP!', end='\n\n\n')
                time.sleep(2)

                if pokemon2.vida < 1:
                    print(f'{pokemon2.nome} desmaiou!!\n\n{pokemon1.nome} é o(a) vencedor(a)!')
                    return pokemon1.nome
                ############################







    

            
                

            


    




## */----------------------------------------------------------------------\* ##



    
