# from pathlib import Path

# import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI",
    version="0.1.0",
)


@app.get('/')
def home():
    return {
        "message": "Hello my friend"
    }


# if __name__ == "__main__":
#     uvicorn.run(f'{Path(__file__).stem}:app', reload=True)
