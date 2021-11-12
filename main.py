from fastapi import FastAPI
from stocks.routers import stocks

app = FastAPI()

app.include_router(stocks.router)