import pandas as pd
import json
df = pd.read_excel('ML Main/traning.xlsx')
counts = []
disc = df.iloc[:,1]
# for x in disc:
#     print(x)
f = open('test2.json')
dic = json.load(f)
print(dic)
for x in disc:
    count = 0
    x = x.lower()
    y = x.split()
    for z in y:
        # print(z)
       if z in dic.keys():
            count += int(dic[z])
    counts.append(count)

dp = pd.DataFrame(counts)
dp.to_excel('ML Main/test_dump.xlsx')