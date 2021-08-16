from fastapi import FastAPI
import uvicorn

from routers import (
    predict
)

from events.event_handlers import (
    start_app_handler,
    stop_app_handler
)

app = FastAPI(
    title = 'Modium Clases'
)

app.include_router(predict.router)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = "0.0.0.0", 
        port = 5000, 
        log_level = "debug"
    )