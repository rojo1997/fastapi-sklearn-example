from fastapi import APIRouter, Query
from starlette.requests import Request
from typing import List
from sklearn.linear_model import SGDClassifier
import numpy as np

router = APIRouter()

@router.get("/predict")
def get_predict(
    request: Request,
    sepalLength: float = Query(1.0),
    sepalWidth: float = Query(1.0),
    petalLength: float = Query(1.0),
    petalWidth: float = Query(1.0)
) -> int:
    clf: SGDClassifier = request.app.state.model
    data = np.array([
        sepalLength,
        sepalWidth,
        petalLength,
        petalWidth
    ]).reshape(1,-1)
    print(data.shape)
    return clf.predict(data).tolist()[0]
