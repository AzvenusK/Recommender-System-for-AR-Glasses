# Libraries
import uvicorn ##ASGI
from fastapi import FastAPI

# App Object
app = FastAPI()

# Index route, opens automatically at port
@app.get('/')
def index():
    return {'message': 'Hello World!'}



