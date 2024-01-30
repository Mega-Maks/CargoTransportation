import os.path
import json
import pyexcel_ods
import Way


class DataBase:

    def __init__(self, pwd: str):
        settings_file_path = f'{pwd}/FileSettings.json'
        settings_file = open(settings_file_path)
        settings_file_data = json.load(settings_file)
        self.ResultDocsDirectoryPath = settings_file_data['ResultDocsDirectory']
        self.InputWaysPath = settings_file_data['InputWays']
        self.DataBaseDirectoryPath = settings_file_data['DataBaseDirectory']
        self.Ways = []
        self.Days = []

    """def check(self, pwd: str):
        settings_file_path = f'{pwd}/FileSettings.json'
        if os.path.isfile(settings_file_path):
            settings_file = open(settings_file_path)
            settings_file_data = json.load(settings_file)


            if 'DataBase' in settings_file_data and \
                    'InputWays' in settings_file_data and \
                    'ResultDocsDirectory' in settings_file_data:
                if os.path.isfile(settings_file_data['DataBase']) and \
                        os.path.isfile(settings_file_data['InputWays']) and \
                        os.path.isdir(settings_file_data['ResultDocsDirectory']):
                    self.DataBasePath = settings_file_data['DataBase']
                    self.InputWaysPath = settings_file_data['InputWays']
                    self.ResultDocsDirectoryPath = settings_file_data['ResultDocsDirectory']
                    self.Check = True
                else:
                    raise Exception('FileSettings file contains wrong path')
            else:
                raise Exception('FileSettings file contains wrong structure')
        else:
            raise Exception('FileSettings file does not exist')"""



    def read(self):
        input_ways = pyexcel_ods.read_data(self.InputWaysPath)
        input_ways = input_ways['Ways']
        for way in input_ways:
            self.Ways.append(Way(way))

    def write(self):
        if self.Ways:
            for way in self.Ways:
                self.Days.append(Day(way, self.DataBaseDirectoryPath))

