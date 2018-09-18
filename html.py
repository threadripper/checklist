import requests

payload = {"t": "b", "w": "Python urllib"}
response = requests.get('http://zzk.cnblogs.com/s', params=payload)
# print(response.url)  # 打印 http://zzk.cnblogs.com/s?w=Python+urllib&t=b&AspxAutoDetectCookieSupport=1
print(response.text)


