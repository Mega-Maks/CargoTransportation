from logic import class_and_funcs
import os
import json

#class_and_funcs.clear()
os.chdir("/home/mega-maks/PycharmProjects/CargoTransportation (копия)")
organization = "Нипигормаш"
if organization not in ["Нипигормаш", "Уралвзрывпром", "Байкал"]:
    raise ValueError("Неверное название организации, пожалуста введите одно из: Нипигормаш ; Уралвзрывпром ; Байкал")
"""key = input("Введите ключ[s/m/n] ")
if key == "s":
    document_number = int(input('введите номер документа '))
    act_val = int(input('введите номер акта '))
    money_at_hour = int(input('введите количество денег зарабатываемое в час '))
elif key == "n":
    with open("FileSettings.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    document_number = data[organization]["last_document_number"] + 1
    act_val = data[organization]["last_act_number"] + 1
    money_at_hour = data[organization]["last_money_at_hour"]
elif key == "m":
    with open("FileSettings.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    document_number = data[organization]["last_document_number"] + 1
    act_val = data[organization]["last_act_number"] + 1
    money_at_hour = int(input('введите количество денег зарабатываемое в час '))
    data["Нипигормаш"]["last_money_at_hour"] = money_at_hour
    data["Уралвзрывпром"]["last_money_at_hour"] = money_at_hour
    data["Байкал"]["last_money_at_hour"] = money_at_hour
else:
    raise Exception("Wrong key")"""
money_at_hour = 1800

if __name__ == "__main__":
    with open('input.txt', encoding="utf-8") as input_file:
        input_file = input_file.read()
    if input_file == "":
        exit(0)
    if "\n\t\t\t\t\t\n" in input_file:
        input_file = input_file.split("\n\t\t\t\t\t\n")
    else:
        input_file = input_file.split("\n\n")
    for i in range(len(input_file)):
        input_file[i] = input_file[i].split('\n')
        for j in range(len(input_file[i])):
            input_file[i][j] = input_file[i][j].split('\t')
    for day_list in input_file:
        ex_val = class_and_funcs.Exel(day_list, day_list[0][1], int(day_list[0][-1]) - 1, organization, money_at_hour)
        ex_val.exel_writer()
        date = ex_val.date
        for way_list in day_list:
            docx_file = class_and_funcs.Docx(way_list, date, int(day_list[0][-1]), organization, ex_val.money_at_hour)
            docx_file.docx_writer()
