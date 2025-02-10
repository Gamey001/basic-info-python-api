from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    current_datetime = datetime.now()
    return {"email": "gdashua@gmail.com","current_datetime":current_datetime,"github_url": ""}

