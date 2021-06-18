import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://frostyworks:Hamilt10@cluster0.5vnhv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.menu

student_collection = database.get_collection("menu_collection")