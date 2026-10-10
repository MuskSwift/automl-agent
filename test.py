from agent.models import get_model
from smolagents import CodeAgent

agent = CodeAgent(tools=[], model=get_model())
print(agent.run("计算斐波那契数列第20项"))
