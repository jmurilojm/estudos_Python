class Carro:
    __ano = None
    cor = None
    
    def setAno(self, ano):
        self.__ano = ano
    def getAno(self):
        return self.__ano
        
    
    def infor(self):
        print(self.__ano,self.cor)
        
    
    
