from app.services.agent_service import run_agent


def test_run_agent_success():
    result = run_agent("查询订单1001")

    assert result["tool_called"] is True
    assert result["tool_name"] == "query_order"


def test_run_agent_failure():
    result = run_agent("你好")

    assert result["tool_called"] is False
    assert result["tool_name"] is None
