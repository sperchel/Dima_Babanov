# Використовуючи принципи ООП, створіть ієрархію класів для представлення типів даних у мові програмування
# С#/Java/JS/Python.
# При реалізації завдання необхідно створити лише структуру класів зі своїми полями і методами.
# Реалізацію методів робити не потрібно - тільки сигнатура або "hardcode" значення, що обертається
# На оцінку впливатимуть:
# 1) ієрархія та кількість рівнів наслідування (достатньо 3 рівня по одній з гілок);
# 2) коректне використання модифікаторів доступу;
# 3) коректне використання модифікаторів abstract та virtual;


class Language:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f'Language: {self.name}, type: {self.type}'


class CSharp(Language):
    def __init__(self, name, type, version):
        super().__init__(name, type)
        self.version = version

    def __str__(self):
        return f'{super().__str__()}, version: {self.version}'


class Java(Language):
    def __init__(self, name, type, version):
        super().__init__(name, type)
        self.version = version

    def __str__(self):
        return f'{super().__str__()}, version: {self.version}'


class Python(Language):
    def __init__(self, name, type, version):
        super().__init__(name, type)
        self.version = version

    def __str__(self):
        return f'{super().__str__()}, version: {self.version}'


class CSharp1(CSharp):
    def __init__(self, name, type, version, platform):
        super().__init__(name, type, version)
        self.platform = platform

    def __str__(self):
        return f'{super().__str__()}, platform: {self.platform}'
