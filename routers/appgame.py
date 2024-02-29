import json
from fastapi import APIRouter

router = APIRouter(
    prefix="/game",
    tags=["game"],
    responses={404: {"message": "Not found"}}
)


def db_game():
    with open('database/app_game.json', "r") as file:
        data = json.load(file)
        return data
data= db_game()
@router.get("/")
async def game():
    
    return data["response"]["games"]
    
    

@router.get("/{game_id}")
async def get_book(game_id: int):
    return data["response"]["games"][game_id-1]

@router.get("/{game_id}/name")
async def get_book_name(game_id:int):
    return data["response"]["games"][game_id-1]["name"]

# @router.post("/")
# async def add_book(book:Book):
#     book_db.append(book.model_dump())
#     return {"message":"add book complete"}

