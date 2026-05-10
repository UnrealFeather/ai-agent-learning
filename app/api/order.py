from fastapi import APIRouter, Query, Depends
from app.schemas.order import OrderQueryRequest, OrderQueryResponse
from app.services.order_service import query_order

router = APIRouter()


@router.post("/query", response_model=OrderQueryResponse)
def query_order_post(request: OrderQueryRequest):
    print(request)
    return query_order(request.order_id)


@router.get("/query", response_model=OrderQueryResponse)
def query_order_get(request: OrderQueryRequest = Depends()):
    return query_order(request.order_id)
