from tkinter.tix import INTEGER
from mlproject.distance import haversine

def test_haversine_function(): 
    assert round(haversine(1, 2, 2, 4)) == 248
