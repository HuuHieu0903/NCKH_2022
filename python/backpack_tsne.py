import json
from underthesea import pos_tag
# import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

################# backpack #######################
def Npbackpack(sentence):
    backpack = "?"
    if "túi" in sentence: backpack =  "túi"
    if "ví" in sentence: backpack =  "ví"
    if "balo" in sentence: backpack =  "balo"
    if "ba lô" in sentence: backpack =  "ba lô"
    if "điện thoại" in sentence: backpack =  "điện thoại"
    if "đồng hồ" in sentence: backpack =  "đồng hồ"
    
    return backpack

id = 1
dictbackpack = {}
for i in range(len(data)):
    # if data[i]["id"] < id:
    if data[i]["split"] != "test":
        continue
    else:
        backpack = Npbackpack(data[i]["captions"][0])
        if backpack in dictbackpack:
            dictbackpack[backpack] += 1
        else:
            dictbackpack[backpack] = 1
        backpack = Npbackpack(data[i]["captions"][1])
        if backpack in dictbackpack:
            dictbackpack[backpack] += 1
        else:
            dictbackpack[backpack] = 1
        id = id + 1

dictbackpackSorted = sorted(dictbackpack.items(), key=lambda x: x[1], reverse=True)
jsonDict = {}
for x in dictbackpackSorted:
    jsonDict[x[0]] = x[1]

with open("./Json/backpack.json", "w", encoding='utf-8') as outfile:
    json.dump(jsonDict, outfile, ensure_ascii=False)

f.close()
