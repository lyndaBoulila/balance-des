import urllib.request as req
import json
url="http://api.openweathermap.org/data/2.5/weather?q=Poitiers,fr"
u=req.urlopen(url)
content=u.read()
jsonstr=content.decode('ascii')
data=json.loads(jsonstr)
t=data['main']['temp']
print("La témpérature est de {} degrés C".format(t-273.15))