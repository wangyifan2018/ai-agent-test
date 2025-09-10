from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate

llm = ChatOllama(
    model = "qwen3:8b-q4_K_M",
    validate_model_on_init = True,
    # other params ...
)


messages = [
    ("system", "You are a helpful translator. Translate the user sentence to Chinese."),
    ("human", "I love programming."),
]
system_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一个{role}专家，擅长{domain}的问题",
    role="system"
)
human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题： {question}",
    role="user"
)

prompt_template = PromptTemplate.from_template("今天的{something}真不错")
# prompt =  prompt_template.format(something="天气")

chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template,
])
# prompt = chat_prompt_template.format_messages(
#     role="编程",
#     domain="Web开发",
#     question="你擅长什么"
# )
examples_template = "输入： {input}\n 输出： {output}"

examples = [
    {"input": "将'Hello'翻译成中文", "output": "你好"},
    {"input": "将'Goodbye'翻译成中文", "output": "再见"}
]
few_shot_prompt_template = FewShotPromptTemplate(
    examples = examples,
    example_prompt=PromptTemplate.from_template(examples_template),
    prefix="请将以下英文翻译成中文: ",
    suffix="输入：{text}\n输出: ",
    input_variables=["text"],
)


from common import chat_prompt_template, llm
from langchain_core.tools import Tool, tool
from pydantic import BaseModel, Field

class AddInputArgs(BaseModel):
  a: int = Field(description="first number"),
  b: int = Field(description="second number")

@tool(
  description="add two numbers",
  args_schema=AddInputArgs,
  return_direct=False,
)
def add(a, b):
  return a + b

# add_tools = Tool.from_function(
#   func=add,
#   name="add",
#   description="add two input numbers",
# )
def create_calc_tools():
  return [add]

calc_tools = create_calc_tools()

tool_dict = {
  "add": add
}
