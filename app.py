import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=21'

contents = requests.get(url)
response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.findAll('tr', 'table_highlight')
print(data[0])
data = data[0]

sholat = {}
i = 0
for value in data:
    if i > 0:
        time = {
            1: 'subuh',
            2: 'zuhur',
            3: 'ashar',
            4: 'maghrib',
            5: 'isya'
        }

        sholat[time.get(i, 'Nothing')] = value.get_text()
    i += 1

print(sholat)
print(sholat['ashar'])