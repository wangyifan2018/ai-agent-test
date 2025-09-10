# <!--IMPORTS:[{"imported": "Tool", "source": "langchain_core.tools", "docs": "https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html", "title": "Python REPL"}, {"imported": "PythonREPL", "source": "langchain_experimental.utilities", "docs": "https://python.langchain.com/api_reference/experimental/utilities/langchain_experimental.utilities.python.PythonREPL.html", "title": "Python REPL"}]-->

from langchain_core.tools import Tool
from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()

ret = python_repl.run("print(1+1)")

print(ret)
