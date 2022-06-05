class localidade:
    def __int__(self, id, nome, estado, regiao, latitude, longitude):
        self.id = id
        self.nome = nome
        self.estado = estado
        self.regiao = regiao
        self.latitude = latitude
        self.longitude = longitude

class notificacoes_total:
    def __init__(self,id_municipio, id_doenca, casos_confirmados):
        self.id_municipio = id_municipio
        self.id_doenca = id_doenca
        self.casos_confirmados = casos_confirmados

class doencas:
    def __int__(self, nome, descricao, vacina_disp, link):
        self.nome = nome
        self.descricao = descricao
        self.vacina_disp = vacina_disp
        self.link = link    




