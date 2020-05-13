import json


#de cadena a diccionario
partidos ='{"Pumas vs America": {"Marcador":[1,0]}, "Atlas vs Necaxa":{"Marcador" : [1,2]},"Chivas vs Cruz Azul":{"Marcador":[2,3]},"Monterrey vs Santos" : {"Marcador": [null,null]} }'

partidos_dict = json.loads(partidos)

print("objeto JSON")
print(partidos_dict)
print("El tipo de dato es: ", type(partidos_dict))

print("\nMarcador de Atlas vs Necaxa")
print(partidos_dict['Atlas vs Necaxa']['Marcador'])
print(partidos_dict.get('Atlas vs Necaxa').get('Maracdor'))


#de diccionario a cadena

partidos_dict = {'Pachica vs Tigres': {'Marcador' : [3,2]}, 
'Remates':16,
'Faltas':None,
'Pases':660}	

partidos_json = json.dumps(partidos_dict)
print("JSON: \n",partidos_json)
print(type(partidos_json))