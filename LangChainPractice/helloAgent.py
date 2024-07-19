from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from typing import List, Union
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.pydantic_v1 import BaseModel, Field
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.runnables import RunnableLambda


prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful assistant who makes fun of Swift developers."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    HumanMessagePromptTemplate.from_template("{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


import os
API_SECRET_KEY = ""
BASE_URL = ""  # 代理 base-url 记得加上 /v1
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, streaming=True)


agent_tools = [DuckDuckGoSearchRun()]
langchain_agent = create_openai_tools_agent(llm, agent_tools, prompt)
agent_executor = AgentExecutor(agent=langchain_agent, tools=agent_tools, return_intermediate_steps=True)

class Input(BaseModel):
    chat_history: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(default_factory=list)
    input: str

def parse_agent_output(agent_output):
    return agent_output["output"]


result = agent_executor.invoke({
    "input":"hello",
    "chat_history": []
})
print(type(result))
print(result)

chain = (agent_executor | RunnableLambda(parse_agent_output)).with_types(input_type=Input, output_type=str)


from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_playground():
    return RedirectResponse("/playground")


add_routes(app, chain, path="/helloagent", playground_type="chat")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
