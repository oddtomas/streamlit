import streamlit as st

st.set_page_config(page_title="Multipage APP", page_icon="✌")
st.title("Input text to generate your own book!")
st.sidebar.title("Select a page above!")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a character name here:", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You entered:", my_input)
    #pass all of this to Eleonors text generator?
    #then those inputs are saved to a bucket that is retrieved by Vita's image generator
    #this script then pulls those seperated bucket items into a booklike format demo'd on the BucketText.py page.

if "action" not in st.session_state:
    st.session_state["action"] = ""

action = st.text_input("Input an action here:", st.session_state["action"])
submit2 = st.button("Submit2")
if submit2:
    st.session_state["action"] = action
    st.write("You entered:", action)