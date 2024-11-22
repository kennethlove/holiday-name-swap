from fastapi import FastAPI, Request
from .models import Giver
from . import get_givers, pair_givers

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def supply_givers(request: Request):
    givers = await request.json()
    givers = [Giver(**giver_data) for giver_data in givers]
    return {"givers": pair_givers(givers)}


