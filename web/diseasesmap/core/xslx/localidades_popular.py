from threading import local
from classes import *
import pandas as pd


def localidades_popular():
    file_name = 'Dados_IDQBRN.xlsx' # File name
    sheet_name = 4 # 5th sheet
    header = 0 # The header is the 1st row
    Nomes_dos_municipios = []
    id = []
    estados = []
    regioes = []
    latitudes = []
    longitudes = []
    localidades = []

    df = pd.read_excel(file_name, sheet_name = sheet_name, header = header)

    for x in df.Municipio:
        Nomes_dos_municipios.append(x)
    
    for x in df.IBGE:
        id.append(x)
    for x in df.UF:
        estados.append(x)
        if (x == "RO" or x == "AM"  or x == "AC" or x=="RR" or x=="PA" or x=="AP" or x=="TO"):
            regioes.append("Regiao Norte")
        elif (x == "MA" or x == "PI"  or x == "CE" or x=="RN" or x=="PB" or x=="AL" or x=="SE" or x == "BA"):
            regioes.append("Regiao Nordeste")
        elif(x == "MT" or x == "MS"  or x == "GO" or x=="DF"):
            regioes.append("Regiao Centro-Oeste")
        elif(x == "MG" or x == "SP"  or x == "RJ" or x=="ES"):
            regioes.append("Regiao Sudeste")
        else:
            regioes.append("Regiao Sul")

    for x in df.latitude:
        latitudes.append(x)
    for x in df.longitude:
        longitudes.append(x)


    for x in range(5570):
        loc = localidade()
        loc.id = id[x]
        loc.nome = Nomes_dos_municipios[x]
        loc.estado = estados[x]
        loc.regiao = regioes[x]
        loc.latitude = latitudes[x]
        loc.longitude = longitudes[x]
        localidades.append(loc)


    return localidades
