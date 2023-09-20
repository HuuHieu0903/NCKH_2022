import json
from underthesea import pos_tag
# import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

################# shoe #######################
def Npshoe(sentence):
    if sentence[len(sentence) - 1] != ".":
        sentence = sentence + "."
    shoe = ""
    if "giày" in sentence: shoe = "giày"
    if "giày thể thao" in sentence: shoe = "giày thể thao"
    if "giầy thể thao" in sentence: shoe = "giầy thể thao"
    if "dép" in sentence: shoe = "dép"
    if "giày da" in sentence: shoe = "giày da"
    if "tất" in sentence: shoe = "tất"

    if shoe != "":
        pos = pos_tag(sentence)
        for i in range(len(pos)):
            if pos[i][0] == shoe:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        shoe += " " + pos[j][0]
                    else: break
    if shoe == "": return "?"
    return shoe

id = 1
dictshoe = {}
for i in range(len(data)):
    # if data[i]["id"] < id:
    if data[i]["split"] != "test":
        continue
    else:
        shoe = Npshoe(data[i]["captions"][0])
        if shoe in dictshoe:
            dictshoe[shoe] += 1
        else:
            dictshoe[shoe] = 1
        shoe = Npshoe(data[i]["captions"][1])
        if shoe in dictshoe:
            dictshoe[shoe] += 1
        else:
            dictshoe[shoe] = 1
        id = id + 1

dictshoeSorted = sorted(dictshoe.items(), key=lambda x: x[1], reverse=True)
jsonDict = {}
for x in dictshoeSorted:
    jsonDict[x[0]] = x[1]

with open("./Json/shoe.json", "w", encoding='utf-8') as outfile:
    json.dump(jsonDict, outfile, ensure_ascii=False)

f.close()
