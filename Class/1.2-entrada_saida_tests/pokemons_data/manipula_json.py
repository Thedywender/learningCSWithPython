import json

with open("pokemons_data/pokemons.json") as file:
    content = file.read()
    pokemons = json.loads(content)["results"]



grass_type_pokemons = []
for pokemon in pokemons:
    if "Grass" in pokemon["type"]:
        grass_type_pokemons.append(pokemon)


with open("grass_pokemon.json", "w") as file:
   json.dump(grass_type_pokemons, file)

print(grass_type_pokemons[0])

