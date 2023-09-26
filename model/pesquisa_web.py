from typing import Union

class Pesquisa():
   
    pesquisa: str = ""
    limite: str = ""
    
    def __init__(self, pesquisa:str, limite:str):
    
        self.pesquisa = pesquisa
        self.limite = limite