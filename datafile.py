import urllib.request
import json
import time

place='India'

response = urllib.request.urlopen("http://api.weatherapi.com/v1/current.json?key=f97bf394f3934328b4962723212010&q=%s&aqi=no"%(place))
data=json.loads(response.read())
name=data['location']['name']
times=time.ctime(data['location']['localtime_epoch'])
tempinc=data['current']['temp_c']
condtn=data['current']['condition']['text']
