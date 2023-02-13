from typing import List


def minimum(numbers: List[int]) -> int:
    return min(numbers)

def maximum(numbers: List[int]) -> int:
    return max(numbers)

def average(numbers: List[int]) -> int:
    return sum(numbers) / len(numbers)

def median(numbers: List[int]) -> int:
    mid_position = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return sum(sorted(numbers)[mid_position-1:mid_position+1]) / 2
    else:
        return sorted(numbers)[mid_position]

def percentile(numbers: List[int], q: int) -> int:
    i = int(q/100 * len(numbers)) - 1
    if i < 0:
        return 0
    return sorted(numbers)[i]
