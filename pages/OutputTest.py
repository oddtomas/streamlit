import streamlit as st

st.title("OutputTest")

if st.session_state["submitted"]:
    st.write(  st.session_state["my_input"])


