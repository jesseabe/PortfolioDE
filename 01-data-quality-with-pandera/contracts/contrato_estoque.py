import pandera as pa
from pandera.typing.pandas import Series
import pandas as pd				

ID_Material = "ID do material"
Data = "data"
Valor = "Valor do estoque"
Quantidade = "Quantidade do estoque"
UMB = "UMB"

# Create the DataFrameModel class using the valid Python identifiers
class MetricasEstoqueBase(pa.DataFrameModel):
    ID_Material: Series[str]
    Data: Series[pa.Timestamp] 
    Valor: Series[float]
    Quantidade: Series[float]
    UMB: Series[str]

    class Config:
        strict = True
        coerce = True

class MetricasEstoqueOut(pa.DataFrameModel):
    ID_Material: Series[str]
    Data: Series[pa.Timestamp] 
    Valor: Series[float]
    Quantidade: Series[float]
    UMB: Series[str]