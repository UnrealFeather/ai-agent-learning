import json
from pathlib import Path

DATA_PATH = Path("app/data/order.json")


def load_orders() -> list[dict]:
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def query_order(order_id: str) -> dict:
    orders = load_orders()
    for order in orders:
        if order["order_id"] == order_id:
            return {
                "success": True,
                "message": "查询成功",
                "data": order,
            }

    return {
        "success": False,
        "message": "订单不存在",
        "data": None,
    }
