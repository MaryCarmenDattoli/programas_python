import requests

response = requests.get("https://api.frankfurter.app/latest")

print(response.headers['Server'])
print(response.headers['Content-Type'])
print(response.headers['Content-Encoding'])