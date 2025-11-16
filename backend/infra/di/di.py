from backend.infra.repo import CardRepoImpl
from backend.app.usecase import CardNKOService
from backend.app.service import CardNKOServiceImpl
from backend.api.exceptions.error import Error

# Функция для создания и предоставления сервиса карточек
# Используется для внедрения зависимостей через FastAPI Depends
def get_card_service() -> CardNKOService:
    # Создаем конкретную реализацию репозитория (например, работа с базой данных)
    repo = CardRepoImpl()
    # Создаем сервис карточек, передавая ему репозиторий
    service = CardNKOServiceImpl(repo)
    # Возвращаем готовый сервис
    return service

# Функция для предоставления обработчика ошибок
# Используется для внедрения зависимостей через FastAPI Depends
def get_error() -> Error:
    # Создаем экземпляр Error
    error = Error()
    return error
