

# Download image from internet using python
import requests

url = "https://imgs.xkcd.com/comics/python.png"
 
response = requests.get(url)
# print(response.headers)
#                        means write bytes
with open('comic.png', 'wb') as file:
    file.write(response.content)


# with open('comic.png', 'wb') as file:
#     file.write(response.content)



# import requests

# base_url = "https://pokeapi.co/api/v2/"


# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     # This get() method will return response object
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieved data response {response.status_code}")

# pokemon_name = "blastoise"

# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"ID: {pokemon_info.get("id")}")
#     print(f"Name: {pokemon_info.get("name")}")
#     print(f"Height: {pokemon_info.get("height")}")
#     print(f"Weight: {pokemon_info.get("weight")}")

