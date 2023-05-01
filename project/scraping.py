import urllib3
import json
import matplotlib.pyplot
import numpy

http = urllib3.PoolManager()
urlApiIBGE = "http://servicodados.ibge.gov.br/api/v2/censos/nomes/"
response = http.request('GET', urlApiIBGE)
print("Response status: ", response.status)