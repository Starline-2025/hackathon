from ..core.error import Error

LAYER = "Domain/Card"

class CardException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: Card\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class CardServerException(CardException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")
		
class CardsNotFoundException(CardException):
	def __init__(self):
		super().__init__(layer=LAYER, message="Cards not found", error="Not Found Error")
		
