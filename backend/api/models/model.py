from pydantic import BaseModel, ConfigDict

class Card(BaseModel):
	model_config = ConfigDict(
		populate_by_name=True,
	)
	name: str
	category: str
	description: str
	city: str
	website: str
	lat: float
	lng: float
	address: str | None = None
	contacts: str | None = None
	img: str | None = None
	