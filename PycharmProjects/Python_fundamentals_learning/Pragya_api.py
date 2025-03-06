import requests
#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://reqres.in/api/users/2')
#print the response text (the content of the requested file):

print(dir(x))
print(x.text)
print(x.__format__())
print(requests.methodname())