from pydantic import BaseModel
from typing import List

class Pesquisaschema(BaseModel):
    """ Define como um novo processamento a ser inserido, deve ser representada
    """
    pesquisa: str = ""
    limite: int = 0

class PesquisaBuscaPeriodoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no periodo da data.
    """
    pesquisa: str = ""
    limite: int = 0

class ListagemPesquisaSchema(BaseModel):
    """ Define como uma listagem de processamento, que será retornada.
    """
    Pesquisa:List[Pesquisaschema]




    