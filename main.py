from typing import Optional
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
	name: str
	description: Optional[str] = Field(
		None, title='The description of the item', max_length=300
	)
	price: float = Field(..., gt=0, descrition='The price must be greater than zero')
	tax: Optional[float] = None
	tags: list = []


class User(BaseModel):
	username: str
	full_name: Optional[str] = None


@app.put('/items/{item_id}/')
async def update_item(
	item_id: int, item: Item = Body(..., embed=True)):
	results = {'item_id': item_id, 'item': item}
	return results
