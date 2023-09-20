import json
from underthesea import pos_tag
import xlsxwriter
import matplotlib.pyplot as plt

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)
ftxt = open('tabstran.txt', 'w', encoding="utf-8")
workbook = xlsxwriter.Workbook('./Excel/NP_tabtran.xlsx')
worksheet = workbook.add_worksheet()


def NounPhase(sentence):
    ## Head
    if sentence[len(sentence) - 1] != ".":
        sentence = sentence + "."
    head = ""
    if "kính" in sentence: head =  "kính"
    if "mũ" in sentence: head = "mũ"
    if "tóc" in sentence: head = "tóc"
    if "mái tóc" in sentence: head = "mái tóc"
    
    ##upperbody
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
    ## lowerbody
    lowerbody = ""
    if "quần" in sentence: lowerbody = "quần"
    if "quần áo" in sentence: lowerbody = "quần áo"
    if "quần bò" in sentence: lowerbody = "quần bò"
    if "quần đùi" in sentence: lowerbody = "quần đùi"
    if "quần soóc" in sentence: lowerbody = "quần soóc"
    ##shoe
    shoe = ""
    if "giày" in sentence: shoe = "giày"
    if "giày thể thao" in sentence: shoe = "giày thể thao"
    if "giầy thể thao" in sentence: shoe = "giầy thể thao"
    if "dép" in sentence: shoe = "dép"
    if "giày da" in sentence: shoe = "giày da"
    if "tất" in sentence: shoe = "tất"
    ##backpack
    backpack = "?"
    if "túi" in sentence: backpack =  "túi"
    if "ví" in sentence: backpack =  "ví"
    if "balo" in sentence: backpack =  "balo"
    if "ba lô" in sentence: backpack =  "ba lô"
    if "điện thoại" in sentence: backpack =  "điện thoại"
    if "đồng hồ" in sentence: backpack =  "đồng hồ"

    ## pos tag
    pos = pos_tag(sentence)
    if head != "":
        for i in range(len(pos)):
            if pos[i][0] == head:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        head += " " + pos[j][0]
                    else: break
    if head == "": head = "?"

    if upperbody != "":
        for i in range(len(pos)):
            if pos[i][0] == upperbody:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        upperbody += " " + pos[j][0]
                    else: break
    if upperbody == "": upperbody = "?"

    if lowerbody != "":
        for i in range(len(pos)):
            if pos[i][0] == lowerbody:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        lowerbody += " " + pos[j][0]
                    else: break
    if lowerbody == "": lowerbody = "?"

    if shoe != "":
        for i in range(len(pos)):
            if pos[i][0] == shoe:
                for j in range(i + 1, len(pos)):
                    if pos[j][1] != "CH":
                        shoe += " " + pos[j][0]
                    else: break
    if shoe == "": shoe = "?"
    return [head, upperbody, lowerbody, shoe, backpack]

dict = {}
id = 1

for i in range(len(data)):
    if data[i]["id"] < id:
        continue
    np = NounPhase(data[i]["captions"][0])
    if np[0] in dict:
        dict[np[0]] += 1
    else:
        dict[np[0]] = 1
    if np[1] in dict:
        dict[np[1]] += 1
    else:
        dict[np[1]] = 1
    if np[2] in dict:
        dict[np[2]] += 1
    else:
        dict[np[2]] = 1
    if np[3] in dict:
        dict[np[3]] += 1
    else:
        dict[np[3]] = 1
    if np[4] in dict:
        dict[np[4]] += 1
    else:
        dict[np[4]] = 1

    ftxt.write(np[0] + " " + np[1] + " " + np[2] + " " + np[3] + " " + np[4] + " ")

    np = NounPhase(data[i]["captions"][1])
    if np[0] in dict:
        dict[np[0]] += 1
    else:
        dict[np[0]] = 1
    if np[1] in dict:
        dict[np[1]] += 1
    else:
        dict[np[1]] = 1
    if np[2] in dict:
        dict[np[2]] += 1
    else:
        dict[np[2]] = 1
    if np[3] in dict:
        dict[np[3]] += 1
    else:
        dict[np[3]] = 1
    if np[4] in dict:
        dict[np[4]] += 1
    else:
        dict[np[4]] = 1

    ftxt.write(np[0] + " " + np[1] + " " + np[2] + " " + np[3] + " " + np[4] + " ")
    id += 1

# print(dict)
dictSorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)

row = 0
for x in dictSorted:
    worksheet.write(row, 0, x[0])
    worksheet.write(row, 1, x[1])
    row += 1

ftxt.close()
f.close()
workbook.close()