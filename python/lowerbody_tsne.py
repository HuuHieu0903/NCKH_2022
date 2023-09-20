import json
from underthesea import pos_tag
# import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

################# lowerBody #######################
def NpLowerBody(sentence):
    if sentence[len(sentence) - 1] != ".":
        sentence = sentence + "."
    lowerbody = ""
    if "quần" in sentence: lowerbody = "quần"
    if "quần áo" in sentence: lowerbody = "quần áo"
    if "quần bò" in sentence: lowerbody = "quần bò"
    if "quần đùi" in sentence: lowerbody = "quần đùi"
    if "quần soóc" in sentence: lowerbody = "quần soóc"

    if lowerbody != "":
        pos = pos_tag(sentence)
        for i in range(len(pos)):
            if pos[i][0] == lowerbody:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        lowerbody += " " + pos[j][0]
                    else: break
    if lowerbody == "": return "?"
    return lowerbody

id = 1
dictLowerBody = {}
for i in range(len(data)):
    # if data[i]["id"] < id:
    if data[i]["split"] != "test":
        continue
    else:
        lowerbody = NpLowerBody(data[i]["captions"][0])
        if lowerbody in dictLowerBody:
            dictLowerBody[lowerbody] += 1
        else:
            dictLowerBody[lowerbody] = 1
        lowerbody = NpLowerBody(data[i]["captions"][1])
        if lowerbody in dictLowerBody:
            dictLowerBody[lowerbody] += 1
        else:
            dictLowerBody[lowerbody] = 1
        id = id + 1

dictLowerBodySorted = sorted(dictLowerBody.items(), key=lambda x: x[1], reverse=True)
jsonDict = {}
for x in dictLowerBodySorted:
    jsonDict[x[0]] = x[1]

with open("./Json/lowerbody.json", "w", encoding='utf-8') as outfile:
    json.dump(jsonDict, outfile, ensure_ascii=False)

f.close()
