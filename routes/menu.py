from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_menu,
    delete_menu,
    retrieve_menu,
    retrieve_menus,
    update_menu,
)
from app.server.models.Menu import (
    ErrorResponseModel,
    ResponseModel,
    MenuSchema,
    UpdateMenuModel,
)
@router.post("/", response_description="Menu data added into the database")
async def add_menu_data(menu: MenuSchema = Body(...)):
    menu = jsonable_encoder(menu)
    new_menu = await add_menu(menu)
    return ResponseModel(new_menu, "Menu added successfully.")

router = APIRouter()