import requests

BASE = "http://127.0.0.1:5000/"


response = requests.get(BASE + "cc/1")
print(response.json())

input()

response = requests.put(BASE + "cc/2", {"id":2})
print(response.json())

input()

response = requests.delete(BASE + "cc/1")

input()

response = requests.get(BASE + "cc/2")
print(response.json())





"""
I left off having trouble deleting things. Errors from both terminals.

What my real goal is here is to nail down a solid method for fetching, updating/appending and
writing data to the cc_data.sqlite3 database I have created.

Once I do that ^ I'm golden. The ML stuff is easy enough. These api calls
are new to me.

"""