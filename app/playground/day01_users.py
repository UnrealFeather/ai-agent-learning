users = [
    {"id": "u1", "name": "Tom", "age": 18, "role": "student"},
    {"id": "u2", "name": "Jerry", "age": 16, "role": "student"},
    {"id": "u3", "name": "Alice", "age": 24, "role": "teacher"},
]

adult_users = []

for user in users:
    if user["age"] >= 18:
        adult_users.append(user)

print(adult_users)


def is_adult(user: dict) -> bool:
    return user["age"] >= 18


def format_user(user: dict) -> str:
    return f"{user['name']} - {user['age']}岁 - {user['role']}"


for user in users:
    print(format_user(user))
    print("是否成年：", is_adult(user))
