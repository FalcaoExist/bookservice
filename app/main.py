from fastapi import FastAPI
from router.category import router1

app = FastAPI()

app.include_router(router1, prefix="/category", tags=["category"])

@app.get('/helpcheck')
def helpcheck() -> bool :
    return True

