import json
from underthesea import pos_tag
import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

workbook = xlsxwriter.Workbook('./head.xlsx')
worksheet = workbook.add_worksheet()

################ HEAD #######################
def NpHead(sentence):
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
row = 0
dictHead = {}
for i in range(len(data)):
    if data[i]["id"] < id:
        continue
    else:
        flag = False
        head = NpHead(data[i]["captions"][0])
        if head in dictHead:
            dictHead[head] += 1
        else:
            dictHead[head] = 1
        id = id + 1

dictHeadSorted = sorted(dictHead.items(), key=lambda x: x[1], reverse=True)

for x in dictHeadSorted:
    worksheet.write(row, 0, x[0])
    worksheet.write(row, 1, x[1])
    row += 1

height = []
tick_label =[]
left = []
count = 0
for x in dictHeadSorted:
    if x[0] != "?":
        tick_label.append(x[0])
        height.append(x[1])
        left.append(count)
        count += 1
    if count == 20:
        break

plt.figure(figsize=(20,15))
# plt.bar(x=left, height=height, tick_label = tick_label,
#         width = 0.9, color = ['green'])
# # naming the x-axis
# plt.xlabel('Noun Phrase')
# # naming the y-axis
# plt.ylabel('Tần số')
# # plot title
# plt.title('Tấn số xuất hiện Noun Phrase')
# plt.xticks(rotation = 60)
# # function to show the plot
# # plt.show()
# plt.tight_layout()

plt.barh(tick_label[::-1], height[::-1], color=['green'])
# setting label of y-axis
plt.ylabel("Noun Phrase")
# setting label of x-axis
plt.xlabel("Tần số")
plt.title("Tấn số xuất hiện Noun Phrase")
plt.show()

f.close()
workbook.close()