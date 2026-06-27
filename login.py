


import streamlit as st

# 用户注册页面的标题
st.title("Streamlit用户注册页面")

# 添加一条分割线
st.divider()

st.text_input("请输入您的用户名")
st.text_input("请输入您的密码", type="password")
st.number_input("请输入您的年龄", min_value=0, max_value=150, step=1)
st.radio("请选择您的性别", options=["男", "女", "保密"], horizontal=True)
st.slider("请输入您的身高(cm)", min_value=0, max_value=250, step=1, value=160)
button = st.button("确认", type="primary")

if button:    
    st.write("恭喜你，信息注册成功!")

