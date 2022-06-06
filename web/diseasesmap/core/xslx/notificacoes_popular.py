from threading import local
from classes import *
import pandas as pd


def notificacoes_popular():
    file_name = 'Dados_IDQBRN.xlsx' # File na
    sheet_name = 4 # 5th sheet
    header = 0 # The header is the 1st row
    Nomes_dos_municipios = []
    Nomes_das_doencas = []
    casos_confirmados = []
    id = []
    notificacoes_totais = []


    df = pd.read_excel(file_name, sheet_name = sheet_name, header = header)

    for x in df.Municipio:
        Nomes_das_doencas.append("BOTULISMO")
    for x in df.IBGE:
        id.append(x)
    for x in df.BOTULISMO:
        casos_confirmados.append(x)
    for x in range(5570):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("DENGUE")
    for x in df.IBGE:
        id.append(x)
    for x in df.DENGUE:
        casos_confirmados.append(x)
    for x in range(5570, (2*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("LEPTOSPIROSE")
    for x in df.IBGE:
        id.append(x)
    for x in df.LEPTOSPIROSE:
        casos_confirmados.append(x)
    for x in range(2*5570, (3*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)

        
    for x in df.Municipio:
        Nomes_das_doencas.append("HANTAVIROSE")
    for x in df.IBGE:
        id.append(x)
    for x in df.HANTAVIROSE:
        casos_confirmados.append(x)
    for x in range(3*5570, (4*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)

        
    for x in df.Municipio:
        Nomes_das_doencas.append("MENINGITE")
    for x in df.IBGE:
        id.append(x)
    for x in df.MENINGITE:
        casos_confirmados.append(x)
    for x in range(4*5570, (5*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("RAIVA")
    for x in df.IBGE:
        id.append(x)
    for x in df.RAIVA:
        casos_confirmados.append(x)
    for x in range(5*5570, (6*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


        
    for x in df.Municipio:
        Nomes_das_doencas.append("LEISHMANIOSE VISCERAL")
    for x in df.IBGE:
        id.append(x)
    for x in df['LEISHMANIOSE VISCERAL']:
        casos_confirmados.append(x)
    for x in range(6*5570, (7*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)
            
    for x in df.Municipio:
        Nomes_das_doencas.append("LEISHMANIOSE TEGUMENTAR")
    for x in df.IBGE:
        id.append(x)
    for x in df['LEISHMANIOSE TEGUMENTAR']:
        casos_confirmados.append(x)
    for x in range(7*5570, (8*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)

    for x in df.Municipio:
        Nomes_das_doencas.append("FEBRE AMARELA")
    for x in df.IBGE:
        id.append(x)
    for x in df['FEBRE AMARELA']:
        casos_confirmados.append(x)
    for x in range(8*5570, (9*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)

    for x in df.Municipio:
        Nomes_das_doencas.append("HEPATITE VIRAL")
    for x in df.IBGE:
        id.append(x)
    for x in df['HEPATITE VIRAL']:
        casos_confirmados.append(x)
    for x in range(9*5570, (10*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("FEBRE MACULOSA")
    for x in df.IBGE:
        id.append(x)
    for x in df['FEBRE MACULOSA']:
        casos_confirmados.append(x)
    for x in range(10*5570, (11*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("DOENÇA DE CHAGAS")
    for x in df.IBGE:
        id.append(x)
    for x in df['DOENÇA DE CHAGAS']:
        casos_confirmados.append(x)
    for x in range(11*5570, (12*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)
            

    for x in df.Municipio:
        Nomes_das_doencas.append("PICADAS DE COBRAS")
    for x in df.IBGE:
        id.append(x)
    for x in df['PICADAS DE COBRAS']:
        casos_confirmados.append(x)
    for x in range(12*5570, (13*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)

    for x in df.Municipio:
        Nomes_das_doencas.append("ZIKA VIRUS")
    for x in df.IBGE:
        id.append(x)
    for x in df['ZIKA VÍRUS']:
        casos_confirmados.append(x)
    for x in range(13*5570, (14*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)


    for x in df.Municipio:
        Nomes_das_doencas.append("FEBRE TIFOIDE")
    for x in df.IBGE:
        id.append(x)
    for x in df['FEBRE TIFÓIDE']:
        casos_confirmados.append(x)
    for x in range(14*5570, (15*5570)):
        nt = notificacoes_total(id[x], Nomes_das_doencas[x], casos_confirmados[x])
        notificacoes_totais.append(nt)



    return notificacoes_totais
