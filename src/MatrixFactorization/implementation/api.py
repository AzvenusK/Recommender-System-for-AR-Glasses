# Libraries
import uvicorn ##ASGI
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd

# App Object
app = FastAPI()

# Index route, opens automatically at port
@app.get('/')
def index():
    return {'message': 'Hello World!'}

