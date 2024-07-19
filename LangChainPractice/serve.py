'''
这是一个langserve使用demo

为了为我们的应用程序创建一个服务器，我们将创建一个文件。这将包含我们为应用程序提供服务的逻辑。它由三件事组成：serve.py

    1. 我们刚刚在上面构建的链的定义
    2. 我们的 FastAPI 应用程序
    3. 为链提供服务的路由的定义，这是通过langserve.add_routes

    更多教程参见：https://python.langchain.com/v0.2/docs/tutorials/llm_chain/#serving-with-langserve

'''

#!/usr/bin/env python
import os
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Create prompt template
system_template = "请把下面的内容翻译为 {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
# sparkllm
os.environ["IFLYTEK_SPARK_APP_ID"] = ""
os.environ["IFLYTEK_SPARK_API_KEY"] = ""
os.environ["IFLYTEK_SPARK_API_SECRET"] = ""
#　此处参考：https://www.xfyun.cn/doc/spark/Web.html
os.environ["IFLYTEK_SPARK_API_URL"] = ""
os.environ["IFLYTEK_SPARK_llm_DOMAIN"] = ""

from langchain_community.chat_models import ChatSparkLLM

model = ChatSparkLLM()

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    playground_type="chat"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)