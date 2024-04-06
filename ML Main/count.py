import pandas as pd
import json
df = pd.read_excel('ML Main/traning.xlsx')
counts = []
disc = df.iloc[:,1]
# for x in disc:
#     print(x)
f = open('test1.json')
dic = json.load(f)
for x in disc:
    count = 0
    for y in x:
        y = y.lower()
        if y in dic.keys():
            count += dic[y]
    counts.append(count)

for x in counts:
    print(x)