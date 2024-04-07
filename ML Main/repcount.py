#make a function that returns word count sum
import json
f = open('test2.json')
dic = json.load(f)

def counter(st):
    s = st.split()
    count = 0
    for x in s:
        if x in dic.keys():
            count += int(dic[x])
    return count