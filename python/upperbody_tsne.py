import json
from underthesea import pos_tag
# import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

# workbook = xlsxwriter.Workbook('./upperbody.xlsx')
# worksheet = workbook.add_worksheet()

################# UPPERBODY #######################
def NpUpperBody(sentence):
    if sentence[len(sentence) - 1] != ".":
        sentence = sentence + "."
    upperbody = ""
    if "áo" in sentence: upperbody = "áo"
    if "áo phông" in sentence: upperbody = "áo phông"
    if "áo nỉ" in sentence: upperbody = "áo nỉ"
    if "áo khoác" in sentence: upperbody = "áo khoác"
    if "áo dài" in sentence: upperbody = "áo dài"
    if "áo cộc" in sentence: upperbody = "áo cộc"
    if "áo sơ mi" in sentence: upperbody = "áo sơ mi"
    if "áo phao" in sentence: upperbody = "áo phao"
    if "áo len" in sentence: upperbody = "áo len"
    if "áo gió" in sentence: upperbody = "áo gió"
    if "áo bò" in sentence: upperbody = "áo bò"
    if "áo hoa" in sentence: upperbody = "áo hoa"
    if "áo bó" in sentence: upperbody = "áo bó"
    if "áo thun" in sentence: upperbody = "áo thun"
    if "váy" in sentence: upperbody = "váy"
    if "quần áo" in sentence: upperbody = "quần áo"

    if upperbody != "":
        pos = pos_tag(sentence)
        for i in range(len(pos)):
            if pos[i][0] == upperbody:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        upperbody += " " + pos[j][0]
                    else: break
    if upperbody == "": return "?"
    return upperbody

id = 1
row = 0
dictUpperBody = {}
for i in range(len(data)):
    # if data[i]["id"] < id:
    if data[i]["split"] != "test":
        continue
    else:
        upperBody = NpUpperBody(data[i]["captions"][0])
        if upperBody in dictUpperBody:
            dictUpperBody[upperBody] += 1
        else:
            dictUpperBody[upperBody] = 1
        upperBody = NpUpperBody(data[i]["captions"][1])
        if upperBody in dictUpperBody:
            dictUpperBody[upperBody] += 1
        else:
            dictUpperBody[upperBody] = 1
        id = id + 1
        # if id == 10:
            # break

dictUpperBodySorted = sorted(dictUpperBody.items(), key=lambda x: x[1], reverse=True)
jsonDict = {}
# ftxt = open('upperbody.txt', 'a', encoding="utf-8")
for x in dictUpperBodySorted:
    # worksheet.write(row, 0, x[0])
    # worksheet.write(row, 1, x[1])
    # ftxt.write(x[0] + " ")
    # print(x[0].replace(" ", ""))
    jsonDict[x[0]] = x[1]
    row += 1
# ftxt.close()

with open("./Json/upperbody.json", "w", encoding='utf-8') as outfile:
    json.dump(jsonDict, outfile, ensure_ascii=False)

f.close()
