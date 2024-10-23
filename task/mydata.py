import json, os

class MyData:
    def __init__(self, locale, time):
        self.locale = locale
        self.time = time

    def __str__(self) -> str:
        return f'Locale: {self.locale}, Time: {self.time}'

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def save(self, file_name) -> None:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(self.to_json())

    @staticmethod
    def from_json(json_str) -> 'MyData':
        data = json.loads(json_str)
        if 'locale' not in data or 'time' not in data:
            return None
        return MyData(data['locale'], data['time'])

    @staticmethod
    def read(file_name) -> 'MyData':
        if os.path.exists(file_name) == False:
            return None
        with open(file_name, 'r', encoding='utf-8') as file:
            return MyData.from_json(file.read())
