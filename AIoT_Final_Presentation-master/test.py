import requests
import json
import random
import sys

url = '<Your restful api url>' # 取代成你的 api url

example_data = [
    [2020, 10, 6, 15, 13.52, 230, 226, 20.1, 19.3, 60.1, 41, 42, 749, 750, 6.73, 6.81],
    [2020, 1, 25, 12, 3.91, 229, 226, 6.2, 5.6, 60.1, 36, 39, 770, 770, 1.93, 2.01],
    [2020, 10, 19, 12, 24.94, 233, 230, 36.0, 36.2, 60.5, 44, 49, 754, 738, 12.44, 12.52]
]

req = {}
req['columns'] = ['YEAR', 'MONTH', 'DAY', 'HOUR', 'OPTPWR', 'ACV1', 'ACV2', 'ACCL1', 'ACCL2', 'ACF1', 'IIT', 'IHT', 'DCVL1', 'DCVL2', 'IPA', 'IPB']
req['questions'] = []
for i in range(random.randint(3,8)):
    temp = example_data[i%3]
    req['questions'].append(temp)

resp = ""
try:
    resp = json.loads(requests.post(url, data=json.dumps(req), timeout=30).content)
except:
    print('請檢察您的 API 是否正常運作')
    sys.exit()

if resp == "":
    print('請檢察您的 API 回傳格式是否正確')
    sys.exit()

if len(resp['predictions']) != len(req['questions']):
    print('長度不一樣，請再檢查')
    sys.exit()

print("基礎測試完成，可以教作業了")