import json
from underthesea import pos_tag
import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

workbook = xlsxwriter.Workbook('./lowerbody.xlsx')
worksheet = workbook.add_worksheet()

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
row = 0
dictLowerBody = {}
for i in range(len(data)):
    if data[i]["id"] < id:
        continue
    else:
        flag = False
        lowerBody = NpLowerBody(data[i]["captions"][0])
        if lowerBody in dictLowerBody:
            dictLowerBody[lowerBody] += 1
        else:
            dictLowerBody[lowerBody] = 1
        id = id + 1

dictLowerBodySorted = sorted(dictLowerBody.items(), key=lambda x: x[1], reverse=True)

for x in dictLowerBodySorted:
    worksheet.write(row, 0, x[0])
    worksheet.write(row, 1, x[1])
    row += 1

height = []
tick_label =[]
left = []
count = 0
for x in dictLowerBodySorted:
    if x[0] != "?":
        tick_label.append(x[0])
        height.append(x[1])
        left.append(count)
        count += 1
    if count == 20:
        break

plt.figure(figsize=(20,15))
plt.barh(tick_label[::-1], height[::-1], color=['green'])
# setting label of y-axis
plt.ylabel("Noun Phrase")
# setting label of x-axis
plt.xlabel("Tần số")
plt.title("Tấn số xuất hiện Noun Phrase")
plt.show()

f.close()
workbook.close()