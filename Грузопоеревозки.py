import class_and_funcs
import os
import docx

class_and_funcs.clear()
organization = input('введите название организации ')
if organization not in ["Нипигормаш", "Уралвзрывпром", "Байкал"]:
    raise ValueError("Неверное название организации, пожалуста введите одно из: Нипигормаш ; Уралвзрывпром ; Байкал")
document_number = int(input('введите номер документа '))
act_val = int(input('введите номер акта '))
money_at_hour = int(input('введите количество денег зарабатываемое в час '))

if __name__ == "__main__":
    os.chdir('/CargoTransportation/Грузоперевозки')
    with open('input.txt', encoding="utf-8") as input_file:
        input_file = input_file.read()
    input_file = input_file.split("\n\n")
    for i in range(len(input_file)):
        input_file[i] = input_file[i].split('\n')
        for j in range(len(input_file[i])):
            input_file[i][j] = input_file[i][j].split('\t')
    #input_file = [[way.split('\t') for way in day.split('\n')] for day in input_file.split("\n\t\t\t\t\t\n")]
    for day_list in input_file:
        doc_count = len(day_list) + 1
        ex_val = class_and_funcs.Exel(day_list, act_val, document_number, organization, money_at_hour)
        ex_val.exel_writer()
        date = ex_val.date
        act_val += 1
        document_number += 1
        for way_list in day_list:
            doc = docx.Document('C:\\Users\\Ryzhk\\PycharmProjects\\Грузоперевозки\\Грузоперевозки\\Шаблон_dox.docx')
            docx_file = class_and_funcs.Docx(way_list, date, document_number, organization)
            docx_file.docx_writer()
            document_number += 1

