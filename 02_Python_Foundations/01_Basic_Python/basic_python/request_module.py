import requests

r = requests.get('https://pypi.org/project/requests/', )
print(r.text)
print("this is directed to the python org website - request_module.py:5")