from common import chat_prompt_template, llm
from langchain_core.tools import Tool, tool
from pydantic import BaseModel, Field

class AddInputArgs(BaseModel):
  a: int = Field(description="first number"),
  b: int = Field(description="second number")

@tool(
  description="add two numbers",
  args_schema=AddInputArgs,
  return_direct=True,
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

llm_with_tools = llm.bind_tools(calc_tools)

chain = chat_prompt_template | llm_with_tools

resp = chain.invoke(input={"role": "计算", "domain": "数学计算", "question":" 使用工具计算 100 + 100=?"})

print(resp)

for tool_calls in resp.tool_calls:
  print(tool_calls)

  args = tool_calls["args"]
  print(args)

  func_name = tool_calls["name"]
  print(func_name)

  tool_func = tool_dict[func_name]
  tool_content = tool_func.invoke(args)
  print(tool_content)