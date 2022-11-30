import requests

user_agent = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

# query = {
#     "search_query" : "morning"
# }

# form = {
#     "custemail": "kva@kva", 
#     "custname": "kva", 
#     "custtel": "kva"
# }

# r = requests.get('https://httpbin.org/get', headers=user_agent)
# r = requests.get('https://www.youtube.com/results', headers=user_agent, params=query)
# print(r.status_code)
# print(r.text)

url = 'https://www.shutterstock.com/shutterstock/videos/1007443438/\
preview/stock-footage-switzerland-winter-landscape-aerial-shot-cinematic-flight-over-a-pine-forest-covered-with-snow.webm'
r = requests.get(url, headers=user_agent, stream=True)
print(r.raw.read(10))

# with open("1.webm", "wb") as webfile:
#     for chunk in r.iter_content(chunk_size=1024 * 100):
#         webfile.write(chunk)
#         print("write chunk")
