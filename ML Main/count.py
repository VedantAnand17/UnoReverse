import pandas as pd
import json
df = pd.read_excel('ML Main/traning.xlsx')
counts = []
disc = df.iloc[:,1]
# for x in disc:
#     print(x)
f = open('frequent.json')
dic = json.load(f)
for x in disc:
    count = 0
    x = x.lower()
    y = x.split()
    for z in y:
        if z in dic.keys():
            print("aagaya")
            count += int(dic[z])
    counts.append(count)

for x in counts:
    print(x)