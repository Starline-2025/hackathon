# Создаем собственное исключение, которое наследуется от стандартного Exception
class Error(Exception):
    def __init__(self, message=None):
        # Вызываем конструктор родительского класса Exception
        # Передаем туда сообщение об ошибке (если оно есть)
        super().__init__(message)
