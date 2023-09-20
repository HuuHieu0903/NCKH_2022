import json
from underthesea import pos_tag
# import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

################# head #######################
def Nphead(sentence):
    if sentence[len(sentence) - 1] != ".":
        sentence = sentence + "."
    head = ""
    if "kính" in sentence: head =  "kính"
    if "mũ" in sentence: head = "mũ"
    if "tóc" in sentence: head = "tóc"
    if "mái tóc" in sentence: head = "mái tóc"
    
    if head != "":
        pos = pos_tag(sentence)
        for i in range(len(pos)):
            if pos[i][0] == head:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        head += " " + pos[j][0]
                    else: break
    if head == "": return "?"
    return head

id = 1
dicthead = {}
for i in range(len(data)):
    # if data[i]["id"] < id:
    if data[i]["split"] != "test":
        continue
    else:
        head = Nphead(data[i]["captions"][0])
        if head in dicthead:
            dicthead[head] += 1
        else:
            dicthead[head] = 1
        head = Nphead(data[i]["captions"][1])
        if head in dicthead:
            dicthead[head] += 1
        else:
            dicthead[head] = 1
        id = id + 1

dictheadSorted = sorted(dicthead.items(), key=lambda x: x[1], reverse=True)
jsonDict = {}
for x in dictheadSorted:
    jsonDict[x[0]] = x[1]

with open("./Json/head.json", "w", encoding='utf-8') as outfile:
    json.dump(jsonDict, outfile, ensure_ascii=False)

f.close()
