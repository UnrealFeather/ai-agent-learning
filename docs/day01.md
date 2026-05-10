# 环境准备与项目规范

## 安装开发环境

### 安装内容

```text
Python 3.11+
VS Code / PyCharm
Git
Docker Desktop
Postman / Apifox
Node.js，可选，用于后续前端联调
```

### 验收标准

```bash
python --version
git --version
docker --version
```

都能正常输出版本。

---

## 创建仓库

### 操作

```bash
mkdir ai-agent-learning-backend
cd ai-agent-learning-backend
git init
```

新建：

```text
README.md
.gitignore
```

`.gitignore` 内容：

```text
.venv
.env
__pycache__
.pytest_cache
app/data/chroma_db
app/uploads
*.db
```

### 验收标准

完成第一次提交：

```bash
git add .
git commit -m "init project"
```

---

## 创建 FastAPI 项目骨架

### 创建虚拟环境

```bash
python -m venv .venv
```

Windows：

```bash
.venv\Scripts\activate
```

Mac / Linux：

```bash
source .venv/bin/activate
```

### 安装依赖

```bash
pip install fastapi uvicorn pydantic python-dotenv pytest
pip freeze > requirements.txt
```

### 创建目录

```text
app/
├── main.py
├── api/
├── schemas/
├── services/
├── core/
├── data/
├── playground/
tests/
.env
README.md
requirements.txt
```

### `app/main.py`

```python
from fastapi import FastAPI

app = FastAPI(title="AI Agent Learning Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

### 启动

```bash
uvicorn app.main:app --reload
```

### 验收标准

打开：

```text
http://127.0.0.1:8000/docs
```

能看到 Swagger 页面。

---

### tips

提示脚本不能运行，

```text
执行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
然后重新激活：
.\.venv\Scripts\Activate.ps1
```

---

# Python + FastAPI 基础

目标：完成一个**无大模型版本 Mini Agent Backend**。

最终接口：

```text
GET  /health
POST /chat
POST /orders/query
POST /agent/run
```

---

## Python 数据结构

### 目标

掌握：

```text
变量
list
dict
for
if
```

### 新建文件

```text
app/playground/day01_users.py
```

### 代码

```python
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
```

### 运行

```bash
python app/playground/day01_users.py
```

### 验收标准

输出里只包含 Tom 和 Alice。

---

## 函数封装

### 新建文件

```text
app/playground/day02_functions.py
```

### 代码

```python
def is_adult(user: dict) -> bool:
    return user["age"] >= 18


def format_user(user: dict) -> str:
    return f"{user['name']} - {user['age']}岁 - {user['role']}"


users = [
    {"id": "u1", "name": "Tom", "age": 18, "role": "student"},
    {"id": "u2", "name": "Jerry", "age": 16, "role": "student"},
]

for user in users:
    print(format_user(user))
    print("是否成年：", is_adult(user))
```

### 验收标准

能说清：

```text
is_adult 负责判断
format_user 负责格式化
一个函数只做一件事
```

---

## 订单查询函数

### 新建文件

```text
app/services/order_service.py
```

### 代码

```python
orders = {
    "1001": {
        "order_id": "1001",
        "status": "已发货",
        "amount": 199,
    },
    "1002": {
        "order_id": "1002",
        "status": "待支付",
        "amount": 299,
    },
}


def query_order(order_id: str) -> dict:
    order = orders.get(order_id)

    if not order:
        return {
            "success": False,
            "message": "订单不存在",
            "data": None,
        }

    return {
        "success": True,
        "message": "查询成功",
        "data": order,
    }
```

### 新建测试脚本

```text
app/playground/day03_test_order.py
```

```python
from app.services.order_service import query_order

print(query_order("1001"))
print(query_order("9999"))
```

### 验收标准

```text
1001 查询成功
9999 订单不存在
```

### tips

报错 from app.services.order_service import query_order;
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'app'

```text
执行：
python -m app.playground.day01_test_order
```

---
