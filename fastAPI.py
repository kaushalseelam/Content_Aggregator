from fastapi import FastAPI
from connectSQL import read_data
app = FastAPI()

@app.get('/')
async def read_root():
    return {"Hello":"World"}


@app.get("/api/v2/users")
async def fetch_links():
    return read_data();

#we want a get that displays all the information from the database

   