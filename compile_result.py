import glob
import pandas as pd
import json

print("generated.....")
datas=[]
files = sorted(glob.glob('./result/*.json'))
for file in files:
    with open(file) as json_file:
        data = json.load(json_file)
    datas.append(data)

df = pd.DataFrame(datas)
df.to_csv('results.csv', index=False)
df.to_excel('results.xlsx', index=False)