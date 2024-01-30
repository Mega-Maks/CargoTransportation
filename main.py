from logic import DataBase
import os
import sys


def write_in_db():
    db = DataBase.DataBase()
    db.check(os.getcwd())
    db.read()
    db.write()


def create_docs(organization):
    db = DataBase.DataBase()
    db.check(os.getcwd())
    db.create(organization)


def check_argv(args: list[str]):
    if len(args) == 2 and args[1] == "-w":
        write_in_db()
    elif len(args) == 3 and args[1] == "-c":
        create_docs(args[2])
    else:
        raise Exception("Wrong args")


if __name__ == '__main__':
    """
    запись в бд {
    прочитать из файла
    для каждого пути:
        если есть день то вписать и добавить стоимость
        иначе добавить день
        добавить маршрут
    }
    
    сделать документы {
    все несделаные дни сделать и записаь в папку
    }
    """
    check_argv(sys.argv)

