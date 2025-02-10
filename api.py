from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def index():
    current_datetime = datetime.now()
    return {"email": "gdashua@gmail.com","current_datetime":current_datetime,"github_url": "https://github.com/Gamey001/basic-info-python-api"}

