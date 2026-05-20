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
```

## 测试

```bash
pytest
```
## 第二阶段功能

当前项目已经接入 DeepSeek LLM API，支持：

- 普通 AI 对话
- Prompt 模板管理
- 结构化意图识别
- 面试题生成
- 面试回答评分
- 多轮对话记忆
- SSE 流式响应
- LLM 调用异常兜底

## 环境变量

```env
API_KEY=你的_deepseek_key
MODEL=deepseek-chat