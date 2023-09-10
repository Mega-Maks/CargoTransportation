import class_and_funcs
import os
import json

#class_and_funcs.clear()
os.chdir("C:\\Users\\Ryzhk\\PycharmProjects\\Грузоперевозки\\CargoTransportation")
organization = input('введите название организации ')
if organization not in ["Нипигормаш", "Уралвзрывпром", "Байкал"]:
    raise ValueError("Неверное название организации, пожалуста введите одно из: Нипигормаш ; Уралвзрывпром ; Байкал")
key = input("Введите ключ[s/m/n] ")
if key == "s":
    document_number = int(input('введите номер документа '))
    act_val = int(input('введите номер акта '))
    money_at_hour = int(input('введите количество денег зарабатываемое в час '))
elif key == "n":
    with open("data.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    document_number = data[organization]["last_document_number"] + 1
    act_val = data[organization]["last_act_number"] + 1
    money_at_hour = data[organization]["last_money_at_hour"]
elif key == "m":
    with open("data.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    document_number = data[organization]["last_document_number"] + 1
    act_val = data[organization]["last_act_number"] + 1
    money_at_hour = int(input('введите количество денег зарабатываемое в час '))
    data["Нипигормаш"]["last_money_at_hour"] = money_at_hour
    data["Уралвзрывпром"]["last_money_at_hour"] = money_at_hour
    data["Байкал"]["last_money_at_hour"] = money_at_hour
else:
    raise Exception("Wrong key")

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
        doc_count = len(day_list) + 1
        ex_val = class_and_funcs.Exel(day_list, act_val, document_number, organization, money_at_hour)
        ex_val.exel_writer()
        date = ex_val.date
        act_val += 1
        document_number += 1
        for way_list in day_list:
            docx_file = class_and_funcs.Docx(way_list, date, document_number, organization)
            docx_file.docx_writer()
            document_number += 1
    if key != "s" and input("Всё верно?[y/n]") == "y":
        data[organization]["last_document_number"] = document_number
        data[organization]["last_act_number"] = act_val
        data[organization]["last_money_at_hour"] = money_at_hour
        os.chdir("C:\\Users\\Ryzhk\\PycharmProjects\\Грузоперевозки\\CargoTransportation")
        with open("data.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file)
