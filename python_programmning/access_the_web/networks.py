import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())

mysock.close()

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/2023_London_Marathon')
for line in fhand:
    print(line.decode().strip())

print(fhand.header())