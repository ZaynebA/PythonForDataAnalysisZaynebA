import requests
import json
import pandas as pd
import numpy as np

url = 'http://localhost:5000/api/'

data =[[130.35667,176,144,54590,12.0,27,1537,0,1564,64483,825054,889537,242000,25.0,480,360,29236,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0
],[177.33333000000002,176,144,53707,12.0,37,2091,0,2128,100969,1089548,1190517,539000,29.97,1920,1080,163024,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0
],[368.32,640,480,29096,25.021739999999998,74,9134,0,9208,869558,470067,1339625,242000,25.0,1920,1080,221152,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0
],[311.1,176,144,56416,12.0,113,3620,0,3733,127552,2066350,2193902,56000,24.0,1920,1080,221160,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0
],[750.433,1280,720,794075,13.482667000000001,81,10031,0,10112,3852576,70635013,74487589,3000000,24.0,1280,720,165700,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1
]]

#data= pd.DataFrame(data)

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)