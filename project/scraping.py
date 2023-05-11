import urllib3
import json
import matplotlib.pyplot
import numpy
import csv

http = urllib3.PoolManager()
urlApiIBGE = "http://servicodados.ibge.gov.br/api/v2/censos/nomes/"
response = http.request('GET', urlApiIBGE)
print("Response status: ", response.status)

data_response = response.data.decode('utf-8')
data_response

data_json = json.loads(data_response)
data_json
