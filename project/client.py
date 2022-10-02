from urllib import request
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT  ='app1/data/'

res = requests.get(BASE_URL+ENDPOINT)

data = res.json()
print("Data from django application\n")

print('employee no : ',data['eno'])
print('\nEmployee name: ',data['ename'])
print('\nemployee salary :',data['esal'])

