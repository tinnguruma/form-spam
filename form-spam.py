import requests
import re

url = input('enter url =>')
tm = int(input('How many times? =>'))

send_url = re.sub('viewfor.+', 'formResponse', url)

site_data = requests.get(url)
site_html = site_data.text

id_list = re.findall(r'\d,\[\[(\d+),', site_html)
id_per = list(dict.fromkeys(id_list))

name_list = re.findall(r'%\.@\.\[\d+,&quot;(.*?)&quot;,', site_html) 
name_per = list(dict.fromkeys(name_list))

ans_list = []
payload = {}

for n in range(len(id_per)):
    x = input(name_per[n] + "=>")
    ans_list.append(x)

for m in range(len(id_per)):
    payload.setdefault("entry." + id_per[m],ans_list[m])

print(payload)
print(send_url)

for t in range(tm):
    response = requests.post(send_url, json=payload)
    print(response.status_code)
    print(t)