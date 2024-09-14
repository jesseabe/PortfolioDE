from typing import Optional
from pydantic import BaseModel, PositiveFloat
from enum import Enum
from datetime import date


class CategoriaEnum(str, Enum):
    NumDoc = "N\u00ba doc."
    Centro = "Cen."
    Referencia = "Refer\u00eancia"
    Doc_Compra = "Doc.compra"
    Data_Lancamento = "Dt.lçto."
    Data_Entrada = "Dt.entr."
    EmissFatur = "EmissFatur"
    Fornecedor = "Nome 1"
    Data_Base = "Data base"
    Dia = "Dia1"
    ID_Material = "Material"
    Desc_Material = "Texto breve de material"
    Quantidade = "Quantidade"
    UMB = "UMP"
    UMB_Desc = "UMP.1"
    Montante = "Montante"
    Moeda = "Moeda"
    CPgt = "CPgt"
    Grupo = "Grupo"
    Denominacao = "Denomina\u00e7\u00e3o"
    ClAv = "ClAv."
    Taxa_Cambio = "Taxa c\u00e2mbio"
    Conta_reconsiliacao = "Cta.recon."
    Data_remessa = "Dt.remessa"

    class Config:
        strict = True
        coerce = True


class ProdutoSchema(BaseModel):
    NumDoc:Optional[str]
    Centro: Optional[str]
    Referencia: Optional[str]
    Doc_Compra: Optional[str]
    Data_Lancamento: date
    Data_Entrada: date
    EmissFatur: Optional[str]
    Fornecedor: Optional[str]
    Data_Base: date
    Dia: str
    ID_Material: str
    Desc_Material: Optional[str]
    Quantidade: float
    UMB: Optional[str]
    UMB_Desc: Optional[str]
    Montante: float
    Moeda: Optional[str]
    CPgt: Optional[str]
    Grupo: Optional[str]
    Denominacao: Optional[str]
    ClAv: Optional[str]
    Taxa_Cambio: float
    Conta_reconsiliacao: Optional[str]
    Data_remessa: date