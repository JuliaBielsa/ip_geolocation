import urllib.request
import xml.etree.ElementTree as ET
import os


ipList = [line.rstrip('\n') for line in open('iplist.txt')]
g = open('output.txt','w')

for ip in ipList:

    r = urllib.request.urlopen("http://ip-api.com/xml/"+ip).read()
    with open('output.xml', 'w') as f:
        f.write(r.decode('utf8'))

    root = ET.parse("output.xml").getroot()

    for tag in root.iter('country'):
        country=(tag.text)

    g.write(ip+" "+country)
    g.write("\n")

os.remove("output.xml")
