import datetime

compile_list = []

with open('act_sverka.txt', encoding="utf-8") as input_file:
    input_file = input_file.read()
if input_file == "":
    exit(0)
if "\n\t\t\t\t\t\n" in input_file:
    input_file = input_file.split("\n\t\t\t\t\t\n")
else:
    input_file = input_file.split("\n\n")
for i in range(len(input_file)):
    c=0
    input_file[i] = input_file[i].split('\n')
    for j in range(len(input_file[i])):
        input_file[i][j] = input_file[i][j].split('\t')
        c += int(input_file[i][j][3])
    compile_list.append([input_file[i][0][0]])
    compile_list[-1].append(c)


with open('from_nipigormash.txt', encoding="utf-8") as nipigormash_input_file:
    nipigormash_input_file = nipigormash_input_file.read()
if nipigormash_input_file == "":
    exit(0)


nipigormash_input_file = nipigormash_input_file.split('\n')
for i in range(len(nipigormash_input_file)):
    date_cost_list = []
    date_cost_list.append(nipigormash_input_file[i][15:25])
    date_cost_list.append(nipigormash_input_file[i][30:-3])
    date_cost_list[1] = int(date_cost_list[1][0:-4] + date_cost_list[1][-3:])
    nipigormash_input_file[i] = date_cost_list

print('\nЕсть у них но нет у нас:\n')
for i in nipigormash_input_file:
    bFlag = False
    bcostFlag = False
    for j in compile_list:
        if i[0] == j[0] and not i[1] == j[1]:
            bcostFlag = True
        bFlag = bFlag or (i[0] == j[0] and i[1] == j[1])
        if bFlag:
            break
    if not bFlag:
        if bcostFlag:
            print(i, "Денги не сошлись")
        else:
            print(i, 'Вообще нет')

print('\nЕсть у нас но нет у них:\n')
for i in compile_list:
    bFlag = False
    bcostFlag = False
    for j in nipigormash_input_file:
        if i[0] == j[0] and not i[1] == j[1]:
            bcostFlag = True
        bFlag = bFlag or (i[0] == j[0] and i[1] == j[1])
        if bFlag:
            break
    if not bFlag:
        if bcostFlag:
            print(i, "Денги не сошлись")
        else:
            print(i, 'Вообще нет')