import pymysql
import json
from urllib2 import urlopen
import socks
import socket
import os


socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
soc = socket.socket
socket.socket = socks.socksocket

while True:
    socket.socket = soc
    connection = pymysql.connect(host="127.0.0.1", user="<username>", passwd="<password>", database="tor_ip_table")
    socket.socket = socks.socksocket
    ip = urlopen('http://ipv4.icanhazip.com').read()
    ip = ip.replace('\n','')
    url = 'http://ip-api.com/json/'+ip+'?fields=520191&lang=en'
    response = urlopen(url)
    data = json.load(response)
    IP = ip
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['regionName']
    try:
        print 'Your IP detail\n '
        print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org, region, country, city, IP)
    except:
        print "format error"
    cursor = connection.cursor()
    insert1 = "INSERT INTO ip_info(IP, REGION, COUNTRY, CITY, ORG) VALUES('"+IP+"','"+region+"','"+country+"','"+city+"','"+org+"');"
    try:
        cursor.execute(insert1)
        connection.commit()
        connection.close()
        print "updated database"
    except Exception as e:
        connection.rollback()
        connection.close()
        print "error",e
    os.system("service tor reload")
    
