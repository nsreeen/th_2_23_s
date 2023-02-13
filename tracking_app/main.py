from datetime import datetime
import logging
import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
logging.basicConfig(level=logging.INFO, filename=f"{PROJECT_ROOT}/requests.log")
app = FastAPI(debug=True)

@app.get("/ping")
async def ping() -> str:
    if os.path.exists(f"{PROJECT_ROOT}/tmp/ok"):
        return "Ok"
    raise HTTPException(status_code=503)

@app.get("/img")
async def img() -> int:
    logging.info(f"{datetime.now()} /img request")
    return FileResponse(f"{PROJECT_ROOT}/gif.gif")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
