import socket
print socket.gethostbyname('google.com')
f = open(r"C:\Python27\code\list1.txt", "r")

for url in f :
	url=url.strip()
	try:
		print url , socket.gethostbyname(url)
	except:
		print url