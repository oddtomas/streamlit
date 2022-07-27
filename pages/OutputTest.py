import streamlit as st

st.title("OutputTest")
st.write(  st.session_state["my_input"])
st.write(  st.session_state["action"])