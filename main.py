# Libraries
import src.MatrixFactorization.results.recommender as rec
from fastapi import FastAPI

# App Object
app = FastAPI()

# Index route, opens automatically at port
@app.get('/')
def recommededItems():
    data = rec.recommended_items
    return {"message": data}



