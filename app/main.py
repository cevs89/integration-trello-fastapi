from fastapi import FastAPI

app = FastAPI(title="SpaceX Challenge")


@app.get("/")
def read_root():
    return {"hello": "world"}
