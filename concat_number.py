from fastapi import FastAPI

app = FastAPI()

@app.get("/concat")
async def concat_number(a:str,b:str):
    return {"concatenated": a+b}

    