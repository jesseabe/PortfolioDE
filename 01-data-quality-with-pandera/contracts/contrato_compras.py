import pandera as pa
from pandera.typing.pandas import Series
import pandas as pd				

Doc_compras = "Doc.compra"
Data = "Data"
Fornecedor = "Nome do fornecedor"
ID_material = "ID do material"
Material_desc = "Descricao do material"
Quantidade = "Quantidade"
UMB = "UMP"
Montante = "Montante"
Moeda = "Moeda"
Taxa_Cambio = "Taxa cambio"

# Create the DataFrameModel class using the valid Python identifiers
class MetricasComprasBase(pa.DataFrameModel):
    Doc_compras: Series[str]
    Data: Series[pa.Timestamp] 
    Fornecedor: Series[str]
    ID_material: Series[int]
    Material_desc: Series[str]
    Quantidade: Series[float]
    UMB: Series[str]
    Montante: Series[float]
    Moeda: Series[str]
    Taxa_Cambio: Series[str]

    class Config:
        strict = True
        coerce = True

class MetricasComprasOut(pa.DataFrameModel):
    Doc_compras: Series[str]
    Data: Series[pa.Timestamp] 
    Fornecedor: Series[str]
    ID_material: Series[int]
    Material_desc: Series[str]
    Quantidade: Series[float]
    UMB: Series[str]
    Montante: Series[float]
    Moeda: Series[str]
    Taxa_Cambio: Series[int]