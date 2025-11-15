from ...domain.errors import CardServerException

LAYER = "Infra/Card"

class InvalidGetCards(CardServerException):
	def __init__(self):
		super().__init__(layer=LAYER,message='Invalid get cards')
		
class InvalidCreateCard(CardServerException):
	def __init__(self):
		super().__init__(layer=LAYER,message='Invalid create card')