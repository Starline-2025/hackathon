from pydantic import BaseModel, ConfigDict

# Определяем модель данных "Card" с помощью Pydantic
# Pydantic автоматически валидирует данные и может конвертировать типы
class Card(BaseModel):
    # Настройки конфигурации модели Pydantic
    model_config = ConfigDict(
        populate_by_name=True,  # Позволяет создавать объект модели через имена полей
    )

    # Обязательные поля модели
    name: str           # Название карточки
    category: str       # Категория карточки
    description: str    # Описание
    city: str           # Город
    website: str        # Веб-сайт
    lat: float          # Широта (для геолокации)
    lng: float          # Долгота (для геолокации)

    # Необязательные поля (могут быть None, если данные отсутствуют)
    address: str | None = None    # Адрес
    contacts: str | None = None   # Контактная информация
    img: str | None = None        # Ссылка на изображение карточки
