

from fastapi import APIRouter
import requests
import random

quotes_url='googlesheet_url'
response = requests.get(quotes_url)
data  = response.json()
router = APIRouter(
    prefix="/quotes-api",
    tags=["quotes-api"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
async def get_quotes():

    return data

@router.get("/r/")
async def get_one_quotes():
    random_quote = random.choice(data)
    return {"status":"Responses Success",
        "data":random_quote}

@router.get("/r/{number}")
async def get_number_quotes(number:int):
    try:
        quotes_number = random.sample(data,number)
        return {
            "status":"Responses Success",
            "quotes":quotes_number,
        }

    except:
         return {
            "status":"fail",
            
        }

    
    