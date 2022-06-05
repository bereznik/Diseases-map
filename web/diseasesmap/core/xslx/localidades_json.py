from localidades_popular import *


def localidades_json():
    Json_localidades = []
    Json_localidades = localidades_popular()
    Final_loc_Json = []#array de Json de loc

    with open('localidades.json', 'w') as arquivo:
        arquivo.write("[\n")
        for x in Json_localidades:
            temp_Json = {
                "id":x.id,
                "nome":x.nome,
                "estado":x.estado,
                "regiao":x.regiao,
                "latitude":x.latitude,
                "longitude":x.longitude
            }
            arquivo.write("{\n" + "\"id\":" + "\"" + str(x.id) + "\"" + ",\n" + "\"nome\":" + "\"" + x.nome + "\"" + ",\n" + "\"estado\":"+ "\""+x.estado+"\""+",\n")
            arquivo.write("\"regiao\":" + "\"" + x.regiao + "\"" + ",\n" + "\"latitude\":" + "\"" + str(x.latitude) + "\"" + ",\n" + "\"longitude\":" + "\"" + str(x.longitude) + "\"" + "\n}" )
            if(x.id != 421985):
                arquivo.write(",\n")
            Final_loc_Json.append(temp_Json)
        
        arquivo.write("\n]")

    arquivo.close()
    return Final_loc_Json
