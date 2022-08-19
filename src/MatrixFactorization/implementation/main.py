# Libraries
import recommender
from fastapi import FastAPI

# App Object
app = FastAPI()

# Index route, opens automatically at port
@app.get('/')
def recommededItems():
    data = recommender.recommended_items
    return {data}



