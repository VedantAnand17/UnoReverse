import pandas as pd
df = pd.read_excel('ML Main/traning.xlsx')
counts = []
disc = df.iloc[2]
print(disc)
# for i in range(60):
#     count  = 0
#     for x in df.iloc[i]    