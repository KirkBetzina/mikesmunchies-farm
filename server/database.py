import collections
from typing import Collection
from menu import Menu
import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://frostyworks:Hamilt10@cluster0.5vnhv.mongodb.net/mikes-crunchies-backend?retryWrites=true&w=majority"
# MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.mikesMenu

mikesMenu = database.get_collection("mikes-menu")

async def fetch_one_menu(Food):
    document = await collections.find_one({"Food":Food})
    return document

async def fetch_all_menus():
    menus = []
    cursor = collections.find({})
    async for document in cursor:
        menus.append(Menu(**document))
        return menus

async def create_menu(menu):
    document = menu
    result = await collections.insert_one(document)
    return result

async def update_menu(Food, Description, Price):
    await collections.update_one({"Food":Food},{"$set":{"Description": Description},})
    document = await collections.find_one({"Food":Food})
    return document

async def remove_menu(Food):
    await collections.delete_one({"Food": Food})
    return  True