# ypy:compile

interface IFactory:
    show(str)->str
    make(int,int,str)->bool

class Factory:
    def show(self, a:str)->str:    
        pass

    def make(self, a:int, b:int, c:str)->bool:    
        pass