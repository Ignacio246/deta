from fastapi import FastAPI
import pickle

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


filename = "model.save"
model = pickle.load(open(filename,'rb'))
predictions = model.predict([[datos]])

