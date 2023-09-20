import json
import xlsxwriter
import re
import matplotlib.pyplot as plt
from underthesea import pos_tag

# Opening JSON file
f = open('vn3k.json', encoding="utf8")
data = json.load(f)

workbook = xlsxwriter.Workbook('./Excel/count_Noun.xlsx')
worksheet = workbook.add_worksheet()
row = 0
id = 1
################# PERSON ########################


# def isPerson(str):
#     str = str.lower()
#     if str == 'đànông':
#         return True
#     if str == 'thanhniên':
#         return True
#     if str == 'cô':
#         return True
#     if str == 'cậu':
#         return True
#     if str == 'chàng':
#         return True
#     if str == 'ông':
#         return True
#     if str == 'bà':
#         return True
#     if str == 'nữ':
#         return True
#     if str == 'nam':
#         return True
#     if str == 'em':
#         return True
#     if str == 'anh':
#         return True
#     if str == 'bác':
#         return True
#     if str == 'phụnữ':
#         return True
#     if str == 'thiếunữ':
#         return True
#     if str == 'gái':
#         return True
#     if str == 'trai':
#         return True
#     if str == 'emtrai':
#         return True
#     return False


# def person(desc):
#     flag = False
#     for i in range(len(desc[0])):
#         if isPerson(desc[0][i]):
#             worksheet.write(row, 0, desc[0][i].lower())
#             flag = True
#     if flag == False:
#         for i in range(len(desc[1])):
#             if isPerson(desc[1][i]):
#                 worksheet.write(row, 0, desc[1][i].lower())
#                 flag = True
#     if flag == False:
#         worksheet.write(row, 0, "?")


# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         desc = data[i]["processed_tokens"]
#         person(desc=desc)
#         row = row + 1
#         id = id + 1

# ################ UPPERBODY #######################
# def isUpperBody(sentence):
#     if sentence[len(sentence) - 1] != ".":
#         sentence = sentence + "."
#     upperbody = ""
#     if "áo" in sentence: upperbody = "áo"
#     if "áo phông" in sentence: upperbody = "áo phông"
#     if "áo nỉ" in sentence: upperbody = "áo nỉ"
#     if "áo khoác" in sentence: upperbody = "áo khoác"
#     if "áo dài" in sentence: upperbody = "áo dài"
#     if "áo cộc" in sentence: upperbody = "áo cộc"
#     if "áo sơ mi" in sentence: upperbody = "áo sơ mi"
#     if "áo phao" in sentence: upperbody = "áo phao"
#     if "áo len" in sentence: upperbody = "áo len"
#     if "áo gió" in sentence: upperbody = "áo gió"
#     if "áo bò" in sentence: upperbody = "áo bò"
#     if "áo hoa" in sentence: upperbody = "áo hoa"
#     if "áo bó" in sentence: upperbody = "áo bó"
#     if "áo thun" in sentence: upperbody = "áo thun"
#     if "váy" in sentence: upperbody = "váy"
#     if "quần áo" in sentence: upperbody = "quần áo"

#     if upperbody != "":
#         pos = pos_tag(sentence)
#         for i in range(len(pos)):
#             if pos[i][0] == upperbody:
#                 for j in range(i + 1, len(pos)):
#                     if pos[j][1] != "CH":
#                         upperbody += " " + pos[j][0]
#                     else: break
#     if upperbody == "": return "?"
#     return upperbody

# row = 0
# id = 1

# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         flag = False
#         upperBody = isUpperBody(data[i]["captions"][0])
#         if upperBody != "?":
#             worksheet.write(row, 2, upperBody)
#             flag = True
#         if flag == False:
#             upperBody = isUpperBody(data[i]["captions"][1])
#             worksheet.write(row, 2, upperBody)
#         row = row + 1
#         id = id + 1

# ################ LOWERBODY #######################
# def isLowerBody(sentence):
#     if sentence[len(sentence) - 1] != ".":
#         sentence = sentence + "."
#     lowerbody = ""
#     if "quần" in sentence: lowerbody = "quần"
#     if "quần áo" in sentence: lowerbody = "quần áo"
#     if "quần bò" in sentence: lowerbody = "quần bò"
#     if "quần đùi" in sentence: lowerbody = "quần đùi"
#     if "quần soóc" in sentence: lowerbody = "quần soóc"

#     if lowerbody != "":
#         pos = pos_tag(sentence)
#         for i in range(len(pos)):
#             if pos[i][0] == lowerbody:
#                 for j in range(i + 1, len(pos)):
#                     if pos[j][1] != "CH":
#                         lowerbody += " " + pos[j][0]
#                     else: break
#     if lowerbody == "": return "?"
#     return lowerbody

# row = 0
# id = 1

# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         flag = False
#         lowerBody = isLowerBody(data[i]["captions"][0])
#         if lowerBody != "?":
#             worksheet.write(row, 3, lowerBody)
#             flag = True
#         if flag == False:
#             lowerBody = isLowerBody(data[i]["captions"][1])
#             worksheet.write(row, 3, lowerBody)
#         row = row + 1
#         id = id + 1

# ################ SHOE #######################
# def isShoe(sentence):
#     if sentence[len(sentence) - 1] != ".":
#         sentence = sentence + "."
#     shoe = ""
#     if "giày" in sentence: shoe = "giày"
#     if "giày thể thao" in sentence: shoe = "giày thể thao"
#     if "giầy thể thao" in sentence: shoe = "giầy thể thao"
#     if "dép" in sentence: shoe = "dép"
#     if "giày da" in sentence: shoe = "giày da"
#     if "tất" in sentence: shoe = "tất"

#     if shoe != "":
#         pos = pos_tag(sentence)
#         for i in range(len(pos)):
#             if pos[i][0] == shoe:
#                 for j in range(i + 1, len(pos)):
#                     if pos[j][1] != "CH":
#                         shoe += " " + pos[j][0]
#                     else: break
#     if shoe == "": return "?"
#     return shoe

# row = 0
# id = 1

# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         flag = False
#         shoe = isShoe(data[i]["captions"][0])
#         if shoe != "?":
#             worksheet.write(row, 4, shoe)
#             flag = True
#         if flag == False:
#             shoe = isShoe(data[i]["captions"][1])
#             worksheet.write(row, 4, shoe)
#         row = row + 1
#         id = id + 1

# ################ HEAD #######################
# def isHead(sentence):
#     head = ""
#     if "kính" in sentence: head =  "kính"
#     if "mũ" in sentence: head = "mũ"
#     if "tóc" in sentence: head = "tóc"
#     if "mái tóc" in sentence: head = "mái tóc"
    

#     if head != "":
#         pos = pos_tag(sentence)
#         for i in range(len(pos)):
#             if pos[i][0] == head:
#                 for j in range(i + 1, len(pos)):
#                     if pos[j][1] != "CH":
#                         head += " " + pos[j][0]
#                     else: break
#     if head == "": return "?"
#     return head

# row = 0
# id = 1

# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         flag = False
#         head = isHead(data[i]["captions"][0])
#         if head != "?":
#             worksheet.write(row, 1, head)
#             flag = True
#         if flag == False:
#             head = isHead(data[i]["captions"][1])
#             worksheet.write(row, 1, head)
#         row = row + 1
#         id = id + 1

# ################ BACKPACK #######################
# def isBackpack(sentence):
#     backpack = "?"
#     if "túi" in sentence: backpack =  "túi"
#     if "ví" in sentence: backpack =  "ví"
#     if "balo" in sentence: backpack =  "balo"
#     if "ba lô" in sentence: backpack =  "ba lô"
#     if "điện thoại" in sentence: backpack =  "điện thoại"
#     if "đồng hồ" in sentence: backpack =  "đồng hồ"
    
#     return backpack

# row = 0
# id = 1

# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         flag = False
#         backpack = isBackpack(data[i]["captions"][0])
#         if backpack != "?":
#             worksheet.write(row, 5, backpack)
#             flag = True
#         if flag == False:
#             backpack = isBackpack(data[i]["captions"][1])
#             worksheet.write(row, 5, backpack)
#         row = row + 1
#         id = id + 1

############################ count #########################

count = {
    'head' : [
        {
            'tóc' : 0,
            'kính' : 0,
            'mũ' : 0,
            # 'mái tóc' : 0
        },
    ],
    'upperbody': [
        {
            'áo phông': 0,
            'áo nỉ': 0,
            'áo khoác': 0,
            'áo dài': 0,
            'áo cộc': 0,
            'áo sơ mi': 0,
            'áo phao': 0,
            'áo len': 0,
            'áo gió': 0,
            'áo bò': 0,
            'áo hoa': 0,
            'áo bó': 0,
            'áo thun': 0,
            'váy': 0,
            'quần áo': 0,
            'áo': 0,
        }
    ],
    'lowerbody': [
        {
            # 'quần áo': 0,
            'quần bò': 0,
            'quần đùi': 0,
            'quần soóc': 0,
            'quần': 0,
        }
    ],
    'shoe': [
        {
            'giày thể thao': 0,
            # 'giầy thể thao': 0,
            'dép': 0,
            'giày da': 0,
            'tất': 0,
            'giày': 0,
        }
    ],
    'backpack': [
        {
            'túi': 0,
            'ví': 0,
            'balo': 0,
            'điện thoại': 0,
            'đồng hồ': 0,
            # 'ba lô': 0,
        }
    ],
}

id = 1
for i in range(len(data)):
    if data[i]["id"] < id:
    # if False:
        continue
    else:
        desc = data[i]["captions"]
################## count head ################
        for j in count['head'][0]:
            if j in desc[0]:
                count['head'][0][j] += 1
                break
        for j in count['head'][0]:
            if j in desc[1]:
                count['head'][0][j] += 1
                break

################## count upperbody ################
        # flag = False
        for j in count['upperbody'][0]:
            if j in desc[0]:
                count['upperbody'][0][j] += 1
                flag = True
                break
        # if flag == False:
        for j in count['upperbody'][0]:
            if j in desc[1]:
                count['upperbody'][0][j] += 1
                break
################## count lowerbody ################
        # flag = False
        for j in count['lowerbody'][0]:
            if j in desc[0]:
                count['lowerbody'][0][j] += 1
                # flag = True
                break
        # if flag == False:
        for j in count['lowerbody'][0]:
            if j in desc[1]:
                count['lowerbody'][0][j] += 1
                break
################## count shoe ################
        # flag = False
        for j in count['shoe'][0]:
            if j in desc[0]:
                count['shoe'][0][j] += 1
                # flag = True
                break
        # if flag == False:
        for j in count['shoe'][0]:
            if j in desc[1]:
                count['shoe'][0][j] += 1
                break
################## count backpack ################
        # flag = False
        for j in count['backpack'][0]:
            if j in desc[0]:
                count['backpack'][0][j] += 1
                # flag = True
                break
        # if flag == False:
        for j in count['backpack'][0]:
            if j in desc[1]:
                count['backpack'][0][j] += 1
                break

        id = id + 1
row = 0
for n in count:
    for x in count[n][0]:
        worksheet.write(row, 0, x)
        worksheet.write(row, 1, count[n][0][x])
        row += 1

print(count)
# row = 0
# id = 1
# for i in range(len(data)):
#     if data[i]["id"] < id:
#         continue
#     else:
#         desc = data[i]["captions"]
#         fnlwgt = 0
#         for j in count:
#             for t in count[j][0]:
#                 flag = False
#                 if t in desc[0]:
#                     fnlwgt += count[j][0][t]
#                     flag = True
#                 if flag == False:
#                     if t in desc[1]:
#                         fnlwgt += count[j][0][t]
                        
#         worksheet.write(row, 6, fnlwgt)
#         id += 1
#         row += 1

# left = []
# height = []
# tick_label =[]

# for key in count['head'][0]:
#     worksheet.write(row, 0, key)
#     worksheet.write(row, 1, count['head'][0][key])
#     row += 1
#     left.append(row)
#     tick_label.append(key)
#     height.append(count['head'][0][key])

# for key in count['upperbody'][0]:
#     worksheet.write(row, 0, key)
#     worksheet.write(row, 1, count['upperbody'][0][key])
#     row += 1
#     left.append(row)
#     tick_label.append(key)
#     height.append(count['upperbody'][0][key])

# for key in count['lowerbody'][0]:
#     worksheet.write(row, 0, key)
#     worksheet.write(row, 1, count['lowerbody'][0][key])
#     row += 1
#     left.append(row)
#     tick_label.append(key)
#     height.append(count['lowerbody'][0][key])

# for key in count['shoe'][0]:
#     worksheet.write(row, 0, key)
#     worksheet.write(row, 1, count['shoe'][0][key])
#     row += 1
#     left.append(row)
#     tick_label.append(key)
#     height.append(count['shoe'][0][key])

# for key in count['backpack'][0]:
#     worksheet.write(row, 0, key)
#     worksheet.write(row, 1, count['backpack'][0][key])
#     row += 1
#     left.append(row)
#     tick_label.append(key)
#     height.append(count['backpack'][0][key])


# f.close()
# workbook.close()

# plt.figure(figsize=(40,10))
# plt.bar(left, height, tick_label = tick_label,
#         width = 0.9, color = ['green'])
# # naming the x-axis
# plt.xlabel('Noun Phrase')
# # naming the y-axis
# plt.ylabel('Tần số')
# # plot title
# plt.title('Tấn số xuất hiện Noun Phrase')
# plt.xticks(rotation = 45)
# # function to show the plot
# plt.show()

f.close()
workbook.close()