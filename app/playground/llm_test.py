from app.services.intent_service import detect_intent

reply = detect_intent("帮我查订单 1001")
print(reply)
