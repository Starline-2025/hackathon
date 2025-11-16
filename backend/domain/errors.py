from backend.core.error import Error

# Константа, указывающая слой, где происходят ошибки
LAYER = "Domain/Card"

# Базовое исключение для ошибок, связанных с карточками
class CardException(Error):
    def __init__(self, layer: str, message: str, error: str):
        # Форматируем сообщение с указанием слоя, уровня и текста ошибки
        message = f"Domain: Card\nLayer: {layer}\nMessage: {message}\nError: {error}"
        # Вызываем конструктор родительского класса Error
        super().__init__(message)

# Исключение для ошибок сервера, связанных с карточками
class CardServerException(CardException):
    def __init__(self, layer: str, message: str):
        # Используем базовое CardException с фиксированным типом ошибки "Server Error"
        super().__init__(layer=layer, message=message, error="Server Error")

# Исключение, когда карточки не найдены
class CardsNotFoundException(CardException):
    def __init__(self):
        # Используем базовое CardException с фиксированным сообщением и типом ошибки "Not Found Error"
        super().__init__(layer=LAYER, message="Cards not found", error="Not Found Error")
