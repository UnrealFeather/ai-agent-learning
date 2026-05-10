下面给你一版**最终可执行版学习计划 + 实施内容**。
目标不是泛泛学习，而是按天推进，最终完成一个可以写进简历、可以部署、可以演示的 Agent 项目。

---

# 总项目目标

## 项目名称

```text
ai-agent-learning-backend
```

## 最终能力

完成后你应该具备：

```text
1. Python 后端开发能力
2. FastAPI 接口开发能力
3. LLM API 调用能力
4. Prompt 模板管理能力
5. 结构化输出能力
6. Tool Calling / Function Calling 能力
7. RAG 知识库能力
8. Agent SDK / LangGraph 工作流能力
9. Docker 部署能力
10. PostgreSQL / Redis / Celery 工程化能力
11. Agent 测试与评估能力
12. 项目包装和面试表达能力
```

---

# 总周期设计

建议按 **90 天**完成。

```text
第 0 阶段：环境准备与项目规范        Day -2 ~ Day 0
第 1 阶段：Python + FastAPI 基础     Day 1  ~ Day 14
第 2 阶段：LLM API + Prompt          Day 15 ~ Day 28
第 3 阶段：Tool Calling              Day 29 ~ Day 42
第 4 阶段：RAG 知识库                Day 43 ~ Day 56
第 5 阶段：Agent SDK + LangGraph     Day 57 ~ Day 70
第 6 阶段：工程化部署                Day 71 ~ Day 90
```

每天学习节奏：

```text
10 分钟：看当天目标
70 分钟：写代码
25 分钟：运行、调试、测试
15 分钟：写学习记录、提交 Git
```

每天结束必须做：

```bash
git add .
git commit -m "dayXX: 完成当天功能"
```

---

# 阶段 0：环境准备与项目规范

## Day -2：安装开发环境

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

## Day -1：创建 GitHub 仓库

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

## Day 0：创建 FastAPI 项目骨架

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

# 阶段 1：Python + FastAPI 基础

目标：完成一个**无大模型版本 Mini Agent Backend**。

最终接口：

```text
GET  /health
POST /chat
POST /orders/query
POST /agent/run
```

---

## Day 1：Python 数据结构

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

## Day 2：函数封装

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

你能说清：

```text
is_adult 负责判断
format_user 负责格式化
一个函数只做一件事
```

---

## Day 3：订单查询函数

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

---

## Day 4：JSON 文件读取

### 新建文件

```text
app/data/orders.json
```

```json
[
  {
    "order_id": "1001",
    "status": "已发货",
    "amount": 199
  },
  {
    "order_id": "1002",
    "status": "待支付",
    "amount": 299
  }
]
```

### 修改 `order_service.py`

```python
import json
from pathlib import Path

DATA_PATH = Path("app/data/orders.json")


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
```

### 验收标准

Day 3 测试脚本结果不变。

---

## Day 5：Pydantic Schema

### 新建文件

```text
app/schemas/order.py
```

```python
from pydantic import BaseModel


class OrderQueryRequest(BaseModel):
    order_id: str


class OrderInfo(BaseModel):
    order_id: str
    status: str
    amount: int


class OrderQueryResponse(BaseModel):
    success: bool
    message: str
    data: OrderInfo | None = None
```

### 验收标准

```bash
python -c "from app.schemas.order import OrderQueryRequest; print(OrderQueryRequest(order_id='1001'))"
```

不报错。

---

## Day 6：FastAPI 基础服务

### 确认 `app/main.py`

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

`GET /health` 返回：

```json
{
  "status": "ok"
}
```

---

## Day 7：订单查询接口

### 新建文件

```text
app/api/order.py
```

```python
from fastapi import APIRouter
from app.schemas.order import OrderQueryRequest, OrderQueryResponse
from app.services.order_service import query_order

router = APIRouter()


@router.post("/query", response_model=OrderQueryResponse)
def query_order_api(request: OrderQueryRequest):
    return query_order(request.order_id)
```

### 修改 `main.py`

```python
from fastapi import FastAPI
from app.api import order

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["Orders"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

### 验收标准

`POST /orders/query` 请求：

```json
{
  "order_id": "1001"
}
```

返回订单信息。

---

## Day 8：普通聊天接口

### 新建 `app/schemas/chat.py`

```python
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
```

### 新建 `app/services/chat_service.py`

```python
def simple_chat(message: str) -> str:
    if "你好" in message:
        return "你好，我是 Mini Agent。"

    return f"你说的是：{message}"
```

### 新建 `app/api/chat.py`

```python
from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import simple_chat

router = APIRouter()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(reply=simple_chat(request.message))
```

### 修改 `main.py`

```python
from fastapi import FastAPI
from app.api import order, chat

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

### 验收标准

`POST /chat` 输入：

```json
{
  "message": "你好"
}
```

返回：

```json
{
  "reply": "你好，我是 Mini Agent。"
}
```

---

## Day 9：规则版 Agent

### 新建 `app/schemas/agent.py`

```python
from pydantic import BaseModel


class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    reply: str
    tool_called: bool
    tool_name: str | None = None
```

### 新建 `app/services/agent_service.py`

```python
import re
from app.services.order_service import query_order
from app.services.chat_service import simple_chat


def run_agent(message: str) -> dict:
    order_match = re.search(r"\d+", message)

    if "订单" in message and order_match:
        order_id = order_match.group()
        result = query_order(order_id)

        if not result["success"]:
            return {
                "reply": result["message"],
                "tool_called": True,
                "tool_name": "query_order",
            }

        order = result["data"]

        return {
            "reply": f"订单 {order_id} 当前状态是：{order['status']}，金额是 {order['amount']} 元。",
            "tool_called": True,
            "tool_name": "query_order",
        }

    return {
        "reply": simple_chat(message),
        "tool_called": False,
        "tool_name": None,
    }
```

### 新建 `app/api/agent.py`

```python
from fastapi import APIRouter
from app.schemas.agent import AgentRequest, AgentResponse
from app.services.agent_service import run_agent

router = APIRouter()


@router.post("/run", response_model=AgentResponse)
def run_agent_api(request: AgentRequest):
    result = run_agent(request.message)
    return AgentResponse(**result)
```

### 修改 `main.py`

```python
from fastapi import FastAPI
from app.api import order, chat, agent

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(agent.router, prefix="/agent", tags=["Agent"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

### 验收标准

`POST /agent/run`：

```json
{
  "message": "帮我查一下订单 1001"
}
```

返回：

```json
{
  "tool_called": true,
  "tool_name": "query_order"
}
```

---

## Day 10：日志

### 新建 `app/core/logger.py`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("agent-backend")
```

### 修改 `agent_service.py`

增加：

```python
from app.core.logger import logger
```

在 `run_agent` 中加入：

```python
logger.info(f"收到用户输入：{message}")
```

调用工具前加入：

```python
logger.info(f"准备调用工具 query_order，order_id={order_id}")
```

### 验收标准

调用 `/agent/run` 时，终端有日志输出。

---

## Day 11：测试订单工具

### 新建 `tests/test_order_service.py`

```python
from app.services.order_service import query_order


def test_query_order_success():
    result = query_order("1001")

    assert result["success"] is True
    assert result["data"]["order_id"] == "1001"


def test_query_order_not_found():
    result = query_order("9999")

    assert result["success"] is False
    assert result["data"] is None
```

### 运行

```bash
pytest
```

### 验收标准

测试通过。

---

## Day 12：测试 Agent

### 新建 `tests/test_agent_service.py`

```python
from app.services.agent_service import run_agent


def test_agent_should_call_order_tool():
    result = run_agent("帮我查一下订单 1001")

    assert result["tool_called"] is True
    assert result["tool_name"] == "query_order"


def test_agent_should_chat():
    result = run_agent("你好")

    assert result["tool_called"] is False
```

### 验收标准

`pytest` 全部通过。

---

## Day 13：README

### README 内容

````markdown
# AI Agent Learning Backend

这是一个 Python + FastAPI 实现的 Agent 学习项目。

## 当前功能

- 健康检查
- 普通聊天
- 订单查询
- 规则版 Agent
- 单元测试

## 启动方式

```bash
uvicorn app.main:app --reload
````

## 测试

```bash
pytest
```

## 接口

* GET /health
* POST /chat
* POST /orders/query
* POST /agent/run

````

### 验收标准

别人根据 README 能启动项目。

---

## Day 14：第一阶段验收

必须满足：

```text
1. uvicorn app.main:app --reload 能启动
2. /docs 能打开
3. /health 正常
4. /chat 正常
5. /orders/query 正常
6. /agent/run 能判断是否调用 query_order
7. pytest 全部通过
8. README 有说明
````

---

# 阶段 2：LLM API + Prompt + 结构化输出

目标：把规则版 Agent 升级成 LLM 驱动 Agent。

---

## Day 15：OpenAI SDK 和配置

### 安装

```bash
pip install openai
pip freeze > requirements.txt
```

### `.env`

```env
OPENAI_API_KEY=你的_api_key
OPENAI_MODEL=你当前可用的模型
```

### 新建 `app/core/config.py`

```python
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "")


settings = Settings()
```

### 验收标准

```bash
python -c "from app.core.config import settings; print(settings.openai_model)"
```

能输出模型名。

---

## Day 16：封装 LLM Service

### 新建 `app/services/llm_service.py`

```python
from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def ask_llm(prompt: str) -> str:
    response = client.responses.create(
        model=settings.openai_model,
        input=prompt,
    )
    return response.output_text
```

### 新建测试脚本

```text
app/playground/day16_llm_test.py
```

```python
from app.services.llm_service import ask_llm

reply = ask_llm("用一句话解释什么是 AI Agent")
print(reply)
```

### 验收标准

终端能看到模型回答。

---

## Day 17：升级聊天接口

### 修改 `chat_service.py`

```python
from app.services.llm_service import ask_llm


def simple_chat(message: str) -> str:
    prompt = f"""
你是一个 Python Agent 开发学习助手。
请用中文、简洁、清晰地回答用户问题。

用户问题：
{message}
"""
    return ask_llm(prompt)
```

### 验收标准

`POST /chat` 能返回真实 AI 回答。

---

## Day 18：Prompt 模板拆分

### 新建 `app/services/prompt_service.py`

```python
def build_chat_prompt(message: str) -> str:
    return f"""
你是一个 Python Agent 开发学习助手。

回答要求：
1. 使用中文
2. 适合初学者
3. 解释清楚
4. 涉及代码时给出简单示例

用户问题：
{message}
"""


def build_intent_prompt(message: str) -> str:
    return f"""
你是一个 Agent 意图识别模块。

请判断用户输入属于哪种类型：
- chat：普通聊天或技术问答
- query_order：查询订单
- interview：生成面试题、参考答案或面试建议

要求：
- 如果是查询订单，请提取订单号
- 不要编造订单号
- 简短说明判断原因

用户输入：
{message}
"""
```

### 修改 `chat_service.py`

```python
from app.services.llm_service import ask_llm
from app.services.prompt_service import build_chat_prompt


def simple_chat(message: str) -> str:
    return ask_llm(build_chat_prompt(message))
```

### 验收标准

Prompt 不再散落在业务文件中。

---

## Day 19：结构化意图识别

### 修改 `schemas/agent.py`

追加：

```python
from typing import Literal


class IntentResult(BaseModel):
    intent: Literal["chat", "query_order", "interview"]
    need_tool: bool
    tool_name: str | None = None
    order_id: str | None = None
    reason: str
```

### 新建 `app/services/intent_service.py`

```python
from openai import OpenAI
from app.core.config import settings
from app.schemas.agent import IntentResult
from app.services.prompt_service import build_intent_prompt

client = OpenAI(api_key=settings.openai_api_key)


def detect_intent(message: str) -> IntentResult:
    response = client.responses.parse(
        model=settings.openai_model,
        input=build_intent_prompt(message),
        text_format=IntentResult,
    )
    return response.output_parsed
```

### 验收标准

输入：

```text
帮我查订单 1001
```

输出中有：

```text
intent='query_order'
order_id='1001'
```

---

## Day 20：LLM 替换规则判断

### 修改 `agent_service.py`

```python
from app.core.logger import logger
from app.services.intent_service import detect_intent
from app.services.order_service import query_order
from app.services.chat_service import simple_chat


def run_agent(message: str) -> dict:
    logger.info(f"收到用户输入：{message}")

    intent = detect_intent(message)
    logger.info(f"识别意图：{intent.model_dump()}")

    if intent.intent == "query_order" and intent.order_id:
        result = query_order(intent.order_id)

        if not result["success"]:
            return {
                "reply": result["message"],
                "tool_called": True,
                "tool_name": "query_order",
            }

        order = result["data"]

        return {
            "reply": f"订单 {intent.order_id} 当前状态是：{order['status']}，金额是 {order['amount']} 元。",
            "tool_called": True,
            "tool_name": "query_order",
        }

    return {
        "reply": simple_chat(message),
        "tool_called": False,
        "tool_name": None,
    }
```

### 验收标准

输入：

```text
查一下 1001 这个单子
```

也能识别为查询订单。

---

## Day 21 - Day 28：第二阶段剩余任务

| 天数     | 任务                   | 产出                                           |
| ------ | -------------------- | -------------------------------------------- |
| Day 21 | 面试题 Schema           | `app/schemas/interview.py`                   |
| Day 22 | 面试题 Prompt 和 Service | `interview_service.py`                       |
| Day 23 | 面试题 API              | `/interview/questions`、`/interview/evaluate` |
| Day 24 | 多轮对话记忆               | `conversation_service.py`                    |
| Day 25 | 流式 LLM Service       | `stream_llm()`                               |
| Day 26 | 流式接口                 | `/chat/stream`                               |
| Day 27 | LLM 异常处理和重试          | `ask_llm_safe()`                             |
| Day 28 | 第二阶段验收               | 测试 + README 更新                               |

### 第二阶段验收标准

```text
1. /chat 可以调用真实 LLM
2. /chat/stream 可以流式输出
3. /agent/run 使用 LLM 识别意图
4. /interview/questions 可生成面试题
5. /interview/evaluate 可评分
6. llm_service.py 有错误兜底
7. pytest 通过
```

---

# 阶段 3：Tool Calling

目标：让模型自己选择工具，由后端执行工具。

---

## Day 29 - Day 42 任务表

| 天数     | 任务                      | 产出                                           |
| ------ | ----------------------- | -------------------------------------------- |
| Day 29 | 整理工具函数                  | `app/tools/order_tools.py`、`refund_tools.py` |
| Day 30 | 定义工具 Schema             | `tool_schemas.py`                            |
| Day 31 | 让模型返回 tool_call         | playground 测试脚本                              |
| Day 32 | 解析 tool_call            | `tool_call_parser.py`                        |
| Day 33 | 工具执行器                   | `tool_executor.py`                           |
| Day 34 | Tool Calling 闭环脚本       | 用户输入 → 工具 → 最终回答                             |
| Day 35 | 封装 Tool Calling Service | `tool_calling_service.py`                    |
| Day 36 | 升级 `/agent/run`         | 真正使用 Tool Calling                            |
| Day 37 | 工具参数校验                  | `schemas/tools.py`                           |
| Day 38 | 统一工具错误响应                | `core/response.py`                           |
| Day 39 | 工具注册中心                  | `tool_registry.py`                           |
| Day 40 | 执行器接入注册中心               | 删除固定 if else                                 |
| Day 41 | 工具风险等级                  | low / medium / high                          |
| Day 42 | 第三阶段验收                  | 工具选择测试                                       |

### 核心工具列表

```text
query_order
calculate_refund
search_knowledge_base，第四阶段加入
```

### 第三阶段验收标准

```text
1. 模型能选择 query_order
2. 模型能选择 calculate_refund
3. 后端能执行工具
4. 工具结果能返回模型生成最终回答
5. 工具有参数校验
6. 工具有统一错误响应
7. 工具有注册中心
8. 高风险工具不自动执行
```

---

# 阶段 4：RAG 知识库

目标：让 Agent 能读取文档，并基于文档回答问题。

---

## Day 43 - Day 56 任务表

| 天数     | 任务                 | 产出                               |
| ------ | ------------------ | -------------------------------- |
| Day 43 | 准备测试文档             | `company_policy.txt`、`resume.md` |
| Day 44 | 文档解析器              | `document_parser.py`             |
| Day 45 | 文本切分               | `chunk_service.py`               |
| Day 46 | Embedding Service  | `embedding_service.py`           |
| Day 47 | 接入 Chroma          | `vector_store.py`                |
| Day 48 | 写入知识库              | `knowledge_ingest_service.py`    |
| Day 49 | 检索知识库              | `search_chunks()`                |
| Day 50 | RAG Prompt         | `build_rag_prompt()`             |
| Day 51 | RAG Answer Service | `rag_service.py`                 |
| Day 52 | 上传接口               | `/knowledge/upload`              |
| Day 53 | 问答接口               | `/knowledge/ask`                 |
| Day 54 | 返回引用片段             | sources 加 content                |
| Day 55 | RAG 封装成工具          | `search_knowledge_base_tool`     |
| Day 56 | 第四阶段验收             | RAG + Agent 联动                   |

### 第四阶段验收标准

```text
1. 支持 txt / md / pdf 解析
2. 支持 chunk 切分
3. 支持 embedding
4. 支持 Chroma 向量库
5. 支持文档上传
6. 支持知识库问答
7. 回答带 sources
8. RAG 能作为 Agent 工具被调用
```

---

# 阶段 5：Agent SDK + LangGraph

目标：实现多 Agent 和工作流编排。

---

## Day 57 - Day 70 任务表

| 天数     | 任务                            | 产出                        |
| ------ | ----------------------------- | ------------------------- |
| Day 57 | 安装 OpenAI Agents SDK          | 第一个 Agent                 |
| Day 58 | function_tool 接入订单工具          | `order_agent.py`          |
| Day 59 | 接入知识库工具                       | `knowledge_agent.py`      |
| Day 60 | Resume Agent                  | `resume_agent.py`         |
| Day 61 | Interview Agent               | `interview_agent.py`      |
| Day 62 | Manager Agent                 | `manager_agent.py`        |
| Day 63 | Handoff Agent                 | `triage_agent.py`         |
| Day 64 | Agent SDK API                 | `/sdk-agent/run`          |
| Day 65 | Guardrails 规则表                | `security_rules.py`       |
| Day 66 | 安装 LangGraph                  | `simple_graph.py`         |
| Day 67 | 条件分支图                         | `router_graph.py`         |
| Day 68 | Planner → Executor → Reviewer | `career_plan_workflow.py` |
| Day 69 | 工作流 API                       | `/workflow/career-plan`   |
| Day 70 | 第五阶段验收                        | 多 Agent + 工作流             |

### 第五阶段验收标准

```text
1. SDK Agent 可运行
2. Order Agent 可调用工具
3. Knowledge Agent 可调用 RAG
4. Resume Agent 可优化简历
5. Interview Agent 可生成面试题
6. Manager Agent 可调度子 Agent
7. Triage Agent 可 handoff
8. LangGraph 可运行
9. 工作流 API 可运行
```

---

# 阶段 6：工程化部署

目标：让项目从 demo 变成可部署服务。

---

## Day 71 - Day 90 任务表

| 天数     | 任务              | 产出                             |
| ------ | --------------- | ------------------------------ |
| Day 71 | 生产目录整理          | `db/`、`tasks/`、`repositories/` |
| Day 72 | `.env.example`  | 环境变量模板                         |
| Day 73 | Dockerfile      | 容器化 API                        |
| Day 74 | docker-compose  | API + Postgres + Redis         |
| Day 75 | 接入 PostgreSQL   | `db/session.py`                |
| Day 76 | AgentRun 模型     | `db/models.py`                 |
| Day 77 | Alembic 迁移      | `migrations/`                  |
| Day 78 | Repository      | `agent_run_repository.py`      |
| Day 79 | Redis 接入        | `redis_service.py`             |
| Day 80 | 限流              | `rate_limit_service.py`        |
| Day 81 | Celery          | `tasks/celery_app.py`          |
| Day 82 | 异步文档处理          | 上传返回 task_id                   |
| Day 83 | JWT 登录          | `/auth/login`                  |
| Day 84 | 保护 `/agent/run` | 鉴权依赖                           |
| Day 85 | 结构化日志           | JSON log                       |
| Day 86 | 成本统计表           | `model_usage_logs`             |
| Day 87 | Agent 测试集       | `eval_cases.json`              |
| Day 88 | GitHub Actions  | CI                             |
| Day 89 | 部署说明            | README                         |
| Day 90 | 总验收             | Docker + 测试 + 文档               |

### 第六阶段验收标准

```text
1. Dockerfile 可构建
2. docker-compose 可启动 API / Postgres / Redis / Worker
3. PostgreSQL 有 agent_runs 表
4. Redis 可用
5. /agent/run 有鉴权
6. /knowledge/upload 异步处理
7. Celery Worker 可消费任务
8. 有结构化日志
9. 有限流
10. 有 Agent 测试集
11. 有 GitHub Actions
12. README 有部署说明
```

---

# 额外提升模块

下面这些建议穿插在 90 天中完成。

---

## 1. Git 分支管理

每个阶段一个分支：

```bash
git checkout -b stage-1-fastapi-basic
git checkout -b stage-2-llm-api
git checkout -b stage-3-tool-calling
git checkout -b stage-4-rag
git checkout -b stage-5-agent-workflow
git checkout -b stage-6-production
```

每阶段完成打 tag：

```bash
git tag v0.1-mini-agent
git tag v0.2-llm-agent
git tag v0.3-tool-agent
git tag v0.4-knowledge-agent
git tag v0.5-workflow-agent
git tag v0.6-production-agent
```

---

## 2. 每日学习记录模板

新建：

```text
docs/daily/
```

每天写：

````markdown
# Day XX 学习记录

## 今天完成
- [ ] 

## 新增文件
- 

## 运行命令
```bash

````

## 遇到的问题

1.

## 解决方式

1.

## 今日提交

commit:

## 明日任务

````

---

## 3. 排错清单

新建：

```text
docs/troubleshooting.md
````

建议写入：

```text
ModuleNotFoundError:
1. 确认在项目根目录运行
2. 使用 python -m 方式运行
3. 确认 app 目录存在

OPENAI_API_KEY 读取不到:
1. 检查 .env 是否在根目录
2. 检查 load_dotenv()
3. 检查变量名是否一致

模型不调用工具:
1. 检查 tools 是否传入
2. 检查 tool description 是否清楚
3. 检查函数名是否正确
4. 检查用户输入是否符合工具场景

RAG 检索不到:
1. 检查文档是否入库
2. 检查 chunk 是否为空
3. 检查 embedding 是否生成
4. 调整 top_k
5. 调整 chunk_size / overlap
```

---

## 4. 评估集

新建：

```text
evals/
├── tool_call_cases.json
├── rag_cases.json
├── workflow_cases.json
└── run_eval.py
```

示例：

```json
[
  {
    "input": "帮我查订单 1001",
    "expected_tool": "query_order"
  },
  {
    "input": "订单 1001 能退多少钱？",
    "expected_tool": "calculate_refund"
  },
  {
    "input": "根据知识库，试用期有年假吗？",
    "expected_tool": "search_knowledge_base"
  }
]
```

---

## 5. 前端联调，可选但强烈建议

你有前端背景，建议增加一个简单前端项目：

```text
ai-agent-learning-frontend
```

页面：

```text
/chat：普通聊天
/agent：Agent 运行
/knowledge：文档上传 + 知识库问答
/interview：面试题生成
```

前端重点：

```text
SSE 流式响应
工具调用状态展示
RAG sources 展示
文件上传
Markdown 渲染
loading / error 状态
```

这部分非常适合写进简历。

---

# 最终项目结构

完成后项目大概是：

```text
ai-agent-learning-backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── agent.py
│   │   ├── auth.py
│   │   ├── chat.py
│   │   ├── interview.py
│   │   ├── knowledge.py
│   │   ├── order.py
│   │   ├── sdk_agent.py
│   │   └── workflow.py
│   ├── agents/
│   │   ├── interview_agent.py
│   │   ├── knowledge_agent.py
│   │   ├── manager_agent.py
│   │   ├── order_agent.py
│   │   ├── resume_agent.py
│   │   └── triage_agent.py
│   ├── core/
│   │   ├── config.py
│   │   ├── deps.py
│   │   ├── logger.py
│   │   ├── response.py
│   │   ├── security.py
│   │   └── security_rules.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── repositories/
│   │   └── agent_run_repository.py
│   ├── schemas/
│   ├── services/
│   ├── tasks/
│   ├── tools/
│   ├── workflows/
│   ├── data/
│   └── uploads/
├── docs/
├── evals/
├── tests/
├── migrations/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

---

# 最终简历描述参考

```text
AI Agent 学习与实践项目

基于 Python、FastAPI、OpenAI API、Tool Calling、RAG、OpenAI Agents SDK、
LangGraph、PostgreSQL、Redis、Celery 和 Docker 构建 Agent 后端系统。

项目支持普通对话、结构化意图识别、订单工具调用、退款金额计算、知识库文档上传、
Embedding 检索、RAG 问答、面试题生成、多 Agent 调度、工作流编排和 Docker 部署。

负责从 0 搭建后端架构，完成 Prompt 模板管理、工具注册中心、工具参数校验、
RAG sources 引用、异步文档处理、JWT 鉴权、接口限流、结构化日志和 Agent 测试集建设，
提升系统可维护性、可观测性和工程化落地能力。
```

---

# 最重要的执行原则

每天只盯当天任务，不要跳阶段。

```text
先跑通，再优化
先单工具，再多工具
先本地 RAG，再 Agentic RAG
先 demo，再工程化
先完成项目，再包装简历
```

真正完成这个计划后，你不只是“学过 Agent”，而是有一个完整项目可以展示：

```text
能运行
能测试
能上传文档
能调用工具
能走工作流
能部署
能写进简历
能讲清楚技术细节
```
