"""
Здесь слой handler и объявляется router от FastApi

Также надо использовать модели Response и Request из папки models в каждом handlers

Вызывать для работы надо класс CardNKOService из файла app/usecase

Также надо использовать Depends(infra/di функция get_card_service) для вызова сервиса CardNKOService

Сделать надо один handler для приема POST и второй для GET по пути /api/cards
"""