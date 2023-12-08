from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
import pickle

# Load the pretrained model using pickle
with open("/app/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

class PredictionInput(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    island: str
    sex: str

app = FastAPI()
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{fruit}")
async def add_fruit(fruit: str):
    id = collection.insert_one({"fruit": fruit}).inserted_id 
    return {"id": str(id)}

@app.get("/list")
async def list_fruits():
    return {"results": list(collection.find({}, {"_id": False}))}

@app.post("/predict")
def predict(input: PredictionInput):
    print(input)
    print(input.dict())
    # Prepare input data for prediction
    input_df = pd.DataFrame([input.dict()])
    
    # Make prediction
    prediction = model.predict(input_df)[0]

    # Return the predicted species
    return {"prediction": prediction}
    # item_data = jsonable_encoder(item)
    # return item_data