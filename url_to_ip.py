import socket
print socket.gethostbyname('google.com')
f = open("url_list.txt", "r")
foundedIP = open("foundedIP.txt", "w")
unfoundedURL = open("unfoundedURL.txt", "w")

for url in f :
	url=url.strip()
	try:
		ip = socket.gethostbyname(url)
		print url , ip
		
		foundedIP.write(ip)
	except:
		print url
		unfoundedURL.write(url)

foundedIP.close()
unfoundedURL.close()
f.close()

