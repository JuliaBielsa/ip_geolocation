import urllib.request
import xml.etree.ElementTree as ET
import os


ipList = [line.rstrip('\n') for line in open('iplist.txt')]
g = open('output.txt','w')


def localizarIP():
    location = input("Enter the type of location you want (country, region or city): ")

    for ip in ipList:

        r = urllib.request.urlopen("http://ip-api.com/xml/"+ip).read()
        with open('output.xml', 'w') as f:
            f.write(r.decode('utf8'))

        root = ET.parse("output.xml").getroot()
        if(location=="region"):
            for tag in root.iter("regionName"):
                country=(tag.text)
        else:
            for tag in root.iter(location):
                country=(tag.text)

        g.write(ip+" "+country)
        g.write("\n")

for i in range(0,10000):
    try:
        localizarIP()
    except:
        print("Upss looks like you didn't write it correctly, try again!\n")
        continue
    break




os.remove("output.xml")
