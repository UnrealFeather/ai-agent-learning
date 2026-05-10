from pydantic import BaseModel

class OrderQueryRequest(BaseModel):
    order_id: str

class OrderInfo(BaseModel):
    order_id: str
    status: str
    amount: float
    
class OrderQueryResponse(BaseModel):
    success: bool
    message: str
    data: OrderInfo | None = None