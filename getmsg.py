import time
import httpx
from fastapi import FastAPI
from pydantic import BaseModel



class Item(BaseModel):
    message: dict
    wcId:str
webhook = FastAPI() #new webhook server

@webhook.post("/wx/") #set post url root
async def create_item(item: Item): #get webhook item
    print(item)
