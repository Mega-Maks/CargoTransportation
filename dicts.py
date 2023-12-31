world_dates = [
    [0, 1, 6],
    [1, 4, 1],
    [1, 4, 3],
    [1, 4, 6],
    [1, 4, 8],
    [2, 12, 1],
    [3, 37, 3],
    [3, 37, 18],
]

month_dict = {
    1: 'Января',
    2: 'Февраля',
    3: 'Марта',
    4: 'Апреля',
    5: 'Мая',
    6: 'Июня',
    7: 'Июля',
    8: 'Августа',
    9: 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря',
}

organization_dict = {"Нипигормаш": """НАО "НИПИГОРМАШ", ИНН 6679007712,667901001, Свердловская обл, Екатеринбург г, Симская ул, 
дом № 1, офис 19 """,
                     "Уралвзрывпром": """ООО «Уралвзрывпром», ИНН 6658153021,667101001, Свердловская обл, г. Екатеринбург, 
           ул. Шаумяна, д. 81 """,
                     "Байкал": """ООО "БАЙКАЛ", ИНН 6674099798, КПП 667901001, Свердловская обл, г. Екатеринбург, ул. Окружная, 
           строение 3/10, помещение 11 """
                     }

organization_short_dict = {"Нипигормаш": """НАО "НИПИГОРМАШ\"""",
                           "Уралвзрывпром": """ООО "Уралвзрывпром\"""",
                           "Байкал": """ООО "БАЙКАЛ\""""
                           }

B12_thousands_two_dict = {
    1: "тысяча", 2: "тысячи", 3: "тысячи", 4: "тысячи", 5: "тысяч",
    6: "тысяч", 7: "тысяч", 8: "тысяч", 9: "тысяч", 10: "тысяч",
    11: "тысяч", 12: "тысяч", 13: "тысяч", 14: "тысяч", 15: "тысяч",
    16: "тысяч", 17: "тысяч", 18: "тысяч", 19: "тысяч", 20: "тысяч",
    21: "тысяча", 22: "тысячи", 23: "тысячи", 24: "тысячи", 25: "тысяч",
    26: "тысяч", 27: "тысяч", 28: "тысяч", 29: "тысяч", 30: "тысяч",
    31: "тысяча", 32: "тысячи", 33: "тысячи", 34: "тысячи", 35: "тысяч",
    36: "тысяч", 37: "тысяч", 38: "тысяч", 39: "тысяч", 40: "тысяч",
    41: "тысяча", 42: "тысячи", 43: "тысячи", 44: "тысячи", 45: "тысяч",
    46: "тысяч", 47: "тысяч", 48: "тысяч", 49: "тысяч", 50: "тысяч",
    51: "тысяча", 52: "тысячи", 53: "тысячи", 54: "тысячи", 55: "тысяч",
    56: "тысяч", 57: "тысяч", 58: "тысяч", 59: "тысяч", 60: "тысяч",
    61: "тысяча", 62: "тысячи", 63: "тысячи", 64: "тысячи", 65: "тысяч",
    66: "тысяч", 67: "тысяч", 68: "тысяч", 69: "тысяч", 70: "тысяч",
    71: "тысяча", 72: "тысячи", 73: "тысячи", 74: "тысячи", 75: "тысяч",
    76: "тысяч", 77: "тысяч", 78: "тысяч", 79: "тысяч", 80: "тысяч",
    81: "тысяча", 82: "тысячи", 83: "тысячи", 84: "тысячи", 85: "тысяч",
    86: "тысяч", 87: "тысяч", 88: "тысяч", 89: "тысяч", 90: "тысяч",
    91: "тысяча", 92: "тысячи", 93: "тысячи", 94: "тысячи", 95: "тысяч",
    96: "тысяч", 97: "тысяч", 98: "тысяч", 99: "тысяч", 100: "тысяч",
    101: "тысяча", 102: "тысячи", 103: "тысячи", 104: "тысячи", 105: "тысяч",
    106: "тысяч", 107: "тысяч", 108: "тысяч", 109: "тысяч"
}

B12_thousands_dict = {
    1: "Одна", 2: "Две", 3: "Три", 4: "Четыре", 5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять",
    10: "Десять", 11: "Одиннадцать", 12: "Двенадцать", 13: "Тринадцать", 14: "Четырнадцать", 15: "Пятнадцать",
    16: "Шестнадцать", 17: "Семнадцать", 18: "Восемнадцать", 19: "Девятнадцать",
    20: "Двадцать", 21: "Двадцать одна", 22: "Двадцать две", 23: "Двадцать три", 24: "Двадцать четыре",
    25: "Двадцать пять",
    26: "Двадцать шесть", 27: "Двадцать семь", 28: "Двадцать восемь", 29: "Двадцать девять",
    30: "Тридцать", 31: "Тридцать одна", 32: "Тридцать две", 33: "Тридцать три", 34: "Тридцать четыре",
    35: "Тридцать пять",
    36: "Тридцать шесть", 37: "Тридцать семь", 38: "Тридцать восемь", 39: "Тридцать девять",
    40: "Сорок", 41: "Сорок одна", 42: "Сорок две", 43: "Сорок три", 44: "Сорок четыре", 45: "Сорок пять",
    46: "Сорок шесть", 47: "Сорок семь", 48: "Сорок восемь", 49: "Сорок девять",
    50: "Пятьдесят", 51: "Пятьдесят одна", 52: "Пятьдесят две", 53: "Пятьдесят три", 54: "Пятьдесят четыре",
    55: "Пятьдесят пять",
    56: "Пятьдесят шесть", 57: "Пятьдесят семь", 58: "Пятьдесят восемь", 59: "Пятьдесят девять",
    60: "Шестьдесят", 61: "Шестьдесят одна", 62: "Шестьдесят две", 63: "Шестьдесят три", 64: "Шестьдесят четыре",
    65: "Шестьдесят пять",
    66: "Шестьдесят шесть", 67: "Шестьдесят семь", 68: "Шестьдесят восемь", 69: "Шестьдесят девять",
    70: "Семьдесят", 71: "Семьдесят одна", 72: "Семьдесят две", 73: "Семьдесят три", 74: "Семьдесят четыре",
    75: "Семьдесят пять",
    76: "Семьдесят шесть", 77: "Семьдесят семь", 78: "Семьдесят восемь", 79: "Семьдесят девять",
    80: "Восемьдесят", 81: "Восемьдесят одна", 82: "Восемьдесят две", 83: "Восемьдесят три", 84: "Восемьдесят четыре",
    85: "Восемьдесят пять",
    86: "Восемьдесят шесть", 87: "Восемьдесят семь", 88: "Восемьдесят восемь", 89: "Восемьдесят девять",
    90: "Девяносто", 91: "Девяносто одна", 92: "Девяносто две", 93: "Девяносто три", 94: "Девяносто четыре",
    95: "Девяносто пять",
    96: "Девяносто шесть", 97: "Девяносто семь", 98: "Девяносто восемь", 99: "Девяносто девять",
    100: "Сто", 101: "Сто одна", 102: "Сто две", 103: "Сто три", 104: "Сто четыре", 105: "Сто пять",
    106: "Сто шесть", 107: "Сто семь", 108: "Сто восемь", 109: "Сто девять"
}

B12_hundreds_dict = {
    1: " сто",
    2: " двести",
    3: " триста",
    4: " четыреста",
    5: " пятьсот",
    6: " шестьсот",
    7: " семьсот",
    8: " восемьсот",
    9: " девятьсот",
    0: ""
}

tons_dict = {
    1: '1000 кг (Одна)',
    2: '2000 кг (Две)',
    3: '3000 кг (Три)',
    4: '4000 кг (Четыре)',
    5: '5000 кг (Пять)',
    6: '6000 кг (Шесть)',
    7: '7000 кг (Семь)',
    8: '8000 кг (Восемь)',
    9: '9000 кг (Девять)',
    10: '10000 кг (Десять)'
}
