import json


#de cadena a diccionario
partidos ='{"Pumas vs America": {"Marcador":[1,0]}, "Atlas vs Necaxa":{"Marcador" : [1,2]},"Chivas vs Cruz Azul":{"Marcador":[2,3]},"Monterrey vs Santos" : {"Marcador": [null,null]} }'

partidos_dict = json.loads(partidos)

print("objeto JSON")
print(partidos_dict)
print("El tipo de dato es: ", type(partidos_dict))

print("\nMarcador de Atlas vs Necaxa")
print(partidos_dict)['Atlas vs Necaxa']['Marcador']