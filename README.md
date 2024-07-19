# 🦜️🔗LangChain Learning

这个仓库用来记录我的LangChain学习

## 学习历程

> [!NOTE]  
> 我把我整理的PDF学习笔记上传到了该仓库，里面有各个资源的链接🥰🥰🥰。

主要通过官方文档、校内课程以及开源社区对LangChain进行系统学习，经过此次学习，已经初步掌握AI开发的整体架构和思路，也收集到了许多的学习资源和启发思路。

这里推荐在进行LangChain开发之前，先对官方文档进行学习，在那里你可以掌握LangChain开发的一整套生态和技术栈，尤其是LangSmith、LangServe、LangGraph，LangChain本身十分简单，如果你想构建大型项目这三个工具可以有效提升你的开发效率和程序性能

- [🦜🛠️ LangSmith](https://docs.smith.langchain.com/): Trace and evaluate your language model applications and intelligent agents to help you move from prototype to production.
- [🦜🕸️ LangGraph](https://langchain-ai.github.io/langgraph/): Create stateful, multi-actor applications with LLMs. Integrates smoothly with LangChain, but can be used without it.
- [🦜🏓 LangServe](https://python.langchain.com/docs/langserve): Deploy LangChain runnables and chains as REST APIs.

在使用LangServe Playground的chat模式时，我发现该功能似乎对于复杂的Runnable对象支持的不好，并且很难查看到日志和报错文档，这里推荐我发现的一个好东西——Chainlit，它应该是Literal AI生态的一环，负责在线展示你的AI程序，它可以构建一个像OpenAI一样的聊天程序，Literal AI也有像LangSmith这样的调试监控工具，值得探索，最后我还推荐一个社区Medium，这里有很多高质量的关于AI开发的帖子。

- [Chainlit](https://docs.chainlit.io): Chainlit is an open-source async Python framework which allows developers to build scalable Conversational AI or agentic applications.
- [Literal AI](https://docs.getliteral.ai): Literal AI is the go-to LLM evaluation and observability platform built for Developers and Product Owners.

## 实战演练

- [Multi-Agent](https://github.com/Wenjun-Ji/Multi-Agent)：在这个LangChain项目，我基于Prompt和LangChain Agent构建了一个多功能聊天机器人，使用四个自定义工具：RAG、Chat、Search、Calculate。

