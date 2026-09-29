# 三元组知识图谱工具

基于 Python 实现的三元组（实体-关系-实体）增删查工具，知识图谱学习项目。

## 功能
- 三元组添加 / 删除 / 查询（按实体、按关系、邻居方向）
- dataclass 建模：Entity / Relation / Triple
- 生成器惰性查询 + 结构化日志

## 运行
python main.py

## 测试
python -m unittest test -v

## 文件结构
- models.py            数据类（Entity / Relation / Triple）
- KnowledgeGraph.py    图谱容器：增删查、JSON 读写、日志
- main.py              命令行入口
- test.py              unittest 测试
- triple.json          示例数据（20 条 AI 人物关系）

## 下一步
- W5：Pandas 数据清洗与去重（CSV / JSON 转换器）
