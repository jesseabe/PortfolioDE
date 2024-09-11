import pandera as pa
from pandera.typing.pandas import Series
import pandas as pd				

Data = "Data"
ID_Material = "ID do material"
Material_desc = "Descricao do material"
Faturamento = "Venda em reais"

# Create the DataFrameModel class using the valid Python identifiers
class MetricasVendasBase(pa.DataFrameModel):
    Data: Series[pa.Timestamp] 
    ID_Material: Series[int]
    Material_desc: Series[str]
    Faturamento: Series[float]

    class Config:
        strict = True
        coerce = True

class MetricasVendasOut(pa.DataFrameModel):
    Data: Series[pa.Timestamp] 
    ID_Material: Series[int]
    Material_desc: Series[str]
    Faturamento: Series[float]