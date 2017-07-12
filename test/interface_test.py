# -*- coding:utf-8 -*-
import requests

# 查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url,params={'eid':'1'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == "success"