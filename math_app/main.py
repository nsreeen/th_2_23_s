from typing import List

from fastapi import FastAPI

import maths
from models import NumbersRequest, QuantifiedNumbersRequest


app = FastAPI(debug=True)


@app.post("/min")
async def min(request: QuantifiedNumbersRequest) -> int:
    return maths.minimum(request.numbers)

@app.post("/max")
async def max(request: QuantifiedNumbersRequest) -> int:
    return maths.maximum(request.numbers)

@app.post("/avg")
async def avg(request: NumbersRequest) -> float:
    return maths.average(request.numbers)

@app.post("/median")
async def median(request: NumbersRequest) -> float:
    return maths.median(request.numbers)

@app.post("/percentile")
async def percentile(request: QuantifiedNumbersRequest) -> int:
    return maths.percentile(request.numbers, request.quantifier)
