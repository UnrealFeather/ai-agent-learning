from app.services.conversation_service import (
    add_message,
    get_messages,
    clear_messages,
)


def test_add_and_get_messages():
    conversation_id = "test_conv"

    clear_messages(conversation_id)

    add_message(conversation_id, "user", "你好")
    add_message(conversation_id, "assistant", "你好，我是助手")

    messages = get_messages(conversation_id)

    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"

    clear_messages(conversation_id)


def test_message_limit():
    conversation_id = "test_limit"

    clear_messages(conversation_id)

    for index in range(30):
        add_message(conversation_id, "user", f"message {index}")

    messages = get_messages(conversation_id)

    assert len(messages) == 20

    clear_messages(conversation_id)