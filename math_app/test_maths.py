import maths


assert maths.minimum([1, 2, 0, 3, 0]) == 0

assert maths.minimum([1]) == 1

assert maths.minimum([1, 2, 0, 3, -10, -90, -20, 1]) == -90

assert maths.maximum([1, 2, 0, 3]) == 3

assert maths.maximum([1]) == 1

assert maths.average([1, 2, 0]) == 1

assert maths.average([1, 2, 0, 7]) == 2.5

assert maths.average([1]) == 1

assert maths.median([1, 2, 0]) == 1

assert maths.median([1, 2, 0, 7]) == 1.5

assert maths.median([1]) == 1

assert maths.percentile([1, 2, 0, 7], 75) == 2

assert maths.percentile([45, 65,  74, 82, 64, 91, 78, 87, 85, 79, 94, 59, 83, 86, 69, 84, 89, 78, 81, 77], 75) == 85

assert maths.percentile([1], 75) == 0

assert maths.percentile([1], 100) == 1

print("tests passed")
