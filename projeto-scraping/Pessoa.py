class Pessoa():

    def __init__(self, nome, sexo, idade):
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade
    


## */----------------------------------------------------------------------\* ##



    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, value):
        self.__sexo = value
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, value):
        self.__idade = value