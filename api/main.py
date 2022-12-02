from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load

class Features(BaseModel):
    season: int
    mnth: int
    holiday: int
    weekday: int
    workingday: int
    weathersit: int
    temp: float
    hum: float
    windspeed: float

    class Config:
        schema_extra = {
            "example":{
                "season": 3.,
                "mnth":7.,
                "holiday": 0.,
                "weekday": 6.,
                "workingday": 1,
                "temp": 0.686667,
                "atemp": 0.638263,
                "hum": 0.585,
                "windspeed": 0.208342
            }
        }
class Label(BaseModel):
    rentals: float

class Message(BaseModel):
    message: float


app = FastAPI(
    title="Rents for FastAPI",
    description=description,
    version="1.0.0",
    terms_of_service=""
)

@app.post("/rentals",
response_model= Label,
status_code=status.HTTP_200_OK,
summary="Rentals",
description="Rentals",
tags=["Rentals"]
)
async def get_rentals