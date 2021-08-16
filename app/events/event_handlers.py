from typing import Callable
from fastapi import FastAPI
import dill

def _startup_model(app: FastAPI) -> None:
    with open('model/model.pkl', 'rb') as file:
        app.state.model = dill.load(file)

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        _startup_model(app)
    return startup

def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)
    return shutdown