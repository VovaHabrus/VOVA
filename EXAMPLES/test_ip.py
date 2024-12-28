import urllib.request as urllib2
import json

while True:
    ip = input("Яка твоя IP : ?")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print("IP: " + values["query"])
    print("City: " + values["city"])
    print("ISP: " + values["isp"])
    print("Country: " + values["country"])
    print("Region: " + values["region"])
    print("Timezone: " + values["timezone"])
    break

# 91.196.55.138
