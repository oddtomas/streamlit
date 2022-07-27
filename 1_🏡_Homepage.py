import streamlit as st

st.set_page_config(page_title="Multipage APP", page_icon="✌")
st.title("Main page")
st.sidebar.title("Select a page above!")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You entered:", my_input)