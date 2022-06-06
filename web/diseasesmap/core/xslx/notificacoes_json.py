from notificacoes_popular import *


def notificacoes_json():
    Json_notificacoes = []
    Json_notificacoes = notificacoes_popular()
    Final_loc_Json = []#array de Json de notification

    with open('notificacoes.json', 'w') as arquivo:
        arquivo.write("[\n")
        for x in Json_notificacoes:
            temp_Json = {
                "idmunicipio":x.id_municipio,
                "nome-doenca":x.id_doenca,
                "casos":x.casos_confirmados,
            }
            arquivo.write("{\n" + "\"idmunicipio\":" + "\"" + str(x.id_municipio) + "\"" + ",\n" )
            arquivo.write("\"nomedoenca\":" + "\"" + x.id_doenca + "\"" + ",\n" + "\"casos\":"+ "\""+ str(x.casos_confirmados)+"\"" +"\n}")
            if(x.id_municipio != 421985 or x.id_doenca != 'FEBRE TIFOIDE'):
                arquivo.write(",\n")
            Final_loc_Json.append(temp_Json)
        
        arquivo.write("\n]")

    arquivo.close()
    return Final_loc_Json

notificacoes_json()