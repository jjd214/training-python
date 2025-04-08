import requests

# Delete data

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print("\nDELETE response:")
print(response.status_code)


# PUT update data

# update_data = {
#     "id": 1,
#     "title": "Boruto",
#     "body": "lorem ipsum",
#     "userId": 1
# }
# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
# print(response.json())

# # Post create data
# data = {
#     "title": "New Post",
#     "body": "This is the content of the post.",
#     "userId": 1
# }

# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# print("\nPOST response:")
# print(response.status_code)
# print(response.json())

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")


# # Fetch data
# if response.status_code == 200:
#     print(f"status code: {response.status_code}")
#     data = response.json()
#     print(data)
# else:
#     print("failed to fetch data")



    
# import requests

# res = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")

# if res.status_code == 200:
#     print(f"status code: {res.status_code}")
    
#     data = res.json()

#     print(data["text"])

# else:
#     print("failed to fetch data")
