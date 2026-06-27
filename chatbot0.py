
"""
功能：聊天机器人主程序和入口
日期：2025/11/22
作者：张翠山
"""

import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

# 编写左侧侧边栏设置UI布局
with st.sidebar:    
    api_key = st.text_input("请输入您的Bigmodel API Key", type="password")    
    st.markdown("[获取Bigmodel账号的API Key](https://bigmodel.cn/console/overview)")

# 编写主页面(聊天框)布局
st.title("GLM聊天机器人")
st.divider()

# session_state类似于一个字典，暂存历史聊天记录
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你好，我是你的AI助手，请问有什么可以帮助你的？"}]
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)

# 遍历会话状态中的消息，显示在聊天框中
for message in st.session_state["messages"]:    
    print("遍历一条聊天消息")    
    st.chat_message(message["role"]).write(message["content"])

# 添加用户提问聊天框
prompt = st.chat_input("请输入您的问题")
# 处理用户提问之后的逻辑
if prompt:
    # 判断API Key是否为空，为空则提示输入    
    if not api_key:        
        st.warning("请输入您的Bigmodel API Key")        
        st.stop()
    # 将用户提问追加到会话状态中    
    st.session_state["messages"].append({"role": "user", "content":  prompt})    
    # 这时候还不能触发上面的for循环，所以需要手动显示用户提问    
    st.chat_message("user").write(prompt)
    
    with st.spinner("AI助手正在思考..."):        
        # 调用大模型接口，获取回答        
        res = get_chat_response(prompt, memory=st.session_state["memory"], api_key=api_key)
    
    # 将大模型回答追加到会话状态中    
    st.session_state["messages"].append({"role": "ai", "content": res})    
    # 手动显示大模型回答    
    st.chat_message("assistant").write(res)
    
print(f"历史聊天记录的长度:{len(st.session_state['messages'])}")

