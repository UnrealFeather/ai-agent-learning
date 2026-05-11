from app.services.order_service import query_order


def test_query_order_success():
    result = query_order("1001")
    assert result["success"] is True

    assert result["data"]["order_id"] == "1001"


def test_query_order_failure():
    result = query_order("1003")
    assert result["success"] is False
    assert result["message"] == "订单不存在"
    assert result["data"] is None
