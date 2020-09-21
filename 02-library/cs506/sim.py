import math


class DistanceCalculationError(Exception):
    pass

class EuclideanCalculationError(DistanceCalculationError):
    pass

class ManhattanCalculationError(DistanceCalculationError):
    pass

class JaccardCalculationError(DistanceCalculationError):
    pass

class CosineSimCalculationError(DistanceCalculationError):
    pass


def validate_points(x, y, exception_class):
    if not x or not y:
        raise exception_class("lengths must not be zero")
    if len(x) != len(y):
        raise exception_class("lengths must be equal")


def euclidean_dist(x, y):
    validate_points(x, y, exception_class=EuclideanCalculationError)
    distance = 0
    for x_val, y_val in zip(x, y):
        distance += abs(x_val - y_val)
    distance = math.sqrt(distance)
    return distance

def manhattan_dist(x, y):
    validate_points(x, y, exception_class=ManhattanCalculationError)
    distance = 0
    for x_val, y_val in zip(x, y):
        distance += abs(x_val - y_val)
    return distance

def jaccard_dist(x, y):
    validate_points(x, y, exception_class=JaccardCalculationError)
    x_set = set(x)
    y_set = set(y)
    intersection = x_set.intersection(y_set)
    union = x_set.union(y_set)
    return 1 - (len(intersection) / len(union))

def cosine_sim(x, y):
    validate_points(x, y, exception_class=CosineSimCalculationError)
    product = sum([x_val*y_val for x_val, y_val in zip(x,y)])
    x_magnitude = magnitude(x)
    y_magnitude = magnitude(y)
    return product/(x_magnitude * y_magnitude)

def magnitude(v):
    return math.sqrt(sum([x**2 for x in v]))
