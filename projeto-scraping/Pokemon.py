import scraping as sc



class Pokemon():

    def __init__(self, id, nome, poder, vida, ataque, defesa, sp_ataque, sp_defesa, velocidade, tipo):
        self.__id = id
        self.__nome = nome
        self.__poder = poder
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa
        self.__sp_ataque = sp_ataque
        self.__sp_defesa = sp_defesa
        self.__velocidade = velocidade
        self.__tipo = tipo



## */----------------------------------------------------------------------\* ##



    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def poder(self):
        return self.__poder
    
    @poder.setter
    def poder(self, value):
        self.__poder = value
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, value):
        self.__vida = value

    @property
    def ataque(self):
        return self.__ataque
    
    @ataque.setter
    def ataque(self, value):
        self.__ataque = value
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, value):
        self.__defesa = value
    
    @property 
    def sp_ataque(self):
        return self.__sp_ataque
    
    @sp_ataque.setter
    def sp_ataque(self, value):
        self.__sp_ataque = value
    
    @property
    def sp_defesa(self):
        return self.__sp_defesa
    
    @sp_defesa.setter
    def sp_defesa(self, value):
        self.__sp_defesa = value
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, value):
        self.__velocidade = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value



## */----------------------------------------------------------------------\* ##



    def __str__(self):
        # for key, value in vars(self).items():
        #     print(key, value)

        print(f'{"ID":10s} => {self.id}\n{"NOME":10s} => {self.nome}\n{"PODER":10s} => {self.poder}\n{"VIDA":10s} => {self.vida}')
        print(f'{"ATAQUE":10s} => {self.ataque}\n{"DEFESA":10s} => {self.defesa}\n{"SP. ATAQUE":10s} => {self.sp_ataque}')
        print(f'{"SP.DEFESA":10s} => {self.sp_defesa}\n{"VELOCIDADE":10s} => {self.velocidade}\n{"TIPO":10s} => {self.tipo}')
        return ''
        

    def __eq__(self, target):
        if self.ataque == target.ataque:
            return 'Empate'
        return self.nome if self.ataque > target.ataque else target.nome


