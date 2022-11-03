import requests
import os

print(__file__)
url = "https://openit.daycat.space/clash"
user_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
print(f"从{url}获取clash文件...")
response = requests.get(url, headers=user_headers)
print(response.status_code)
print(f'当前工作目录：{os.getcwd()}')
with open('clash_openit.yml', 'w') as f:
    f.write(response.text)
