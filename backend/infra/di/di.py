from ...infra.repo import CardRepoImpl
from ...app.usecase import CardNKOService
from ...app.service import CardNKOServiceImpl


def get_card_service() -> CardNKOService:
    repo = CardRepoImpl()
    service = CardNKOServiceImpl(repo)
    return service