from typing import List

from pydantic import BaseModel, validator


class NumbersRequest(BaseModel):
    numbers: List[int]
    @validator("numbers")
    def numbers_cannot_be_empty(cls, numbers):
        if len(numbers) == 0:
            raise ValueError("Numbers parameter must not be empty list.")
        return numbers

class QuantifiedNumbersRequest(NumbersRequest):
    numbers: List[int]
    quantifier: int
