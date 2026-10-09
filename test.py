from agent.models import get_model
from smolagents import CodeAgent

agent = CodeAgent(tools=[], model=get_model())
print(agent.run("先回答1+1等于几，观察后再回答1+1的10倍和100谁更大"))
