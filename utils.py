
"""
功能：langchain
调用GLM工具类日期：2025/11/22
作者：张翠山
"""

# 导入必要的库
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 导入GLM 模型
from langchain_community.chat_models import ChatZhipuAI

# 封装调用函数
def get_chat_response(prompt, memory, api_key):    
    model = ChatZhipuAI(model="glm-4", api_key=api_key, temperature=0.7)    
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]
    
