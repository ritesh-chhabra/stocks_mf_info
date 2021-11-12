from fastapi import APIRouter, Response, status
from stocks import schemas
from stocks.repository import stock

router = APIRouter(
    prefix = "/stocks",
    tags = ["stocks"]
)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model= schemas.ShowStock)
def show(id, response:Response):
    return stock.show(id)