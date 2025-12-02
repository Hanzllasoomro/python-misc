import requests

# Request Method - GET
x = requests.get("http://api.github.com/users/Hanzllasoomro")
print(x.text)
print(x.status_code)

data = x.json()

print(data)
print("Followers: ", data['followers'])

# api endpoint

url = "http://official-joke-api.appspot.com/jokes/programming/random"
response = requests.get(url)
data = response.json()[0]

for key in data:
    print(key," : ",data[key])

#Resquest Method - POST

myobj = [("Hanzlla", 21), ("Muneeb", 22) ]
r= requests.post("http://httpbin.org/post", data=myobj)
print(r.json())
