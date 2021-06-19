from app.server.models.Menu import Menu
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from starlette.responses import Response
from app.routes.menu import router as MenuRouter 
app = FastAPI()

app.include_router(MenuRouter, tags=["Menu"], prefix="/menu")

from app.server.database import (
    fetch_one_menu,
    fetch_all_menus,
    create_menu,
    update_menu,
    remove_menu,
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.get("/api/menu")
async def get_menu():
    response = await fetch_all_menus
    return response


@app.get("/api/menu{Food}", response_model=Menu)
async def get_menu_by_id(Food):
    response= await fetch_one_menu(Food)
    if response:
        return response
    raise HTTPException(404, "there is no menu item with this name")

@app.post("/api/menu", response_model=Menu)
async def post_menu(menu:Menu):
    response = await create_menu(menu)( dict()) #watch this line, this is probably going to mess up 
    if response:
        return response
    

@app.put("/api/menu{Food}", response_model=Menu)
async def put_menu(Food:str, Description:str, Price: int):
    response = await update_menu(Food, Description, Price)
    if response:
        return response

@app.delete("/api/menu{Food}")
async def delete_menu(Food):
    response = await remove_menu(Food)
    if response:
        return "Food item deleted from menu"

    