import os
from dotenv import load_dotenv
from smolagents import OpenAIModel

load_dotenv()


def get_model(name: str = "glm"):
    if name == "glm":
        return OpenAIModel(
            model_id="glm-5.3",
            api_base="https://open.bigmodel.cn/api/paas/v4",
            api_key=os.environ["ZHIPUAI_API_KEY"],
            reasoning_effort="max",
            max_tokens=65536,
            temperature=1.0,
            extra_body={"thinking": {"type": "enabled"}},
        )
    if name == "":
        return OpenAIModel(
            model_id="",
            api_base="",
            api_key=os.environ[""],
        )
    raise ValueError(name)
