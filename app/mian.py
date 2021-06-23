# from pathlib import Path

# import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI",
    version="0.1.0",
)


@app.get('/')
def home():
    return 'Hello miner bot !!!'


# if __name__ == "__main__":
#     uvicorn.run(f'{Path(__file__).stem}:app', reload=True)
