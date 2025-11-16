from backend.domain.errors import CardServerException

# Константа, указывающая слой, где происходят ошибки
LAYER = "Infra/Card"

# Исключение для ошибок при получении карточек
class InvalidGetCards(CardServerException):
    def __init__(self):
        # Вызываем конструктор родительского класса с указанием слоя и сообщения
        super().__init__(layer=LAYER, message='Invalid get cards')

# Исключение для ошибок при создании карточки
class InvalidCreateCard(CardServerException):
    def __init__(self):
        # Вызываем конструктор родительского класса с указанием слоя и сообщения
        super().__init__(layer=LAYER, message='Invalid create card')
