# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file cloud_images.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    cloud_image = bucket.blob(file_path).download_as_bytes()
    return cloud_image

bucket_name = "thomas-demo-bucket"
file_path = "Clementine.png"

cloud_image = read_file(bucket_name, file_path)

# Print results.
# for line in cloud_image.strip().split("\n"):
#     name, pet = line.split(",")
#     st.write(f"{name} has a :{pet}:")


# st.image(cloud_image)

if "test_image" not in st.session_state:
    st.session_state["test_image"] = ""

test_image = st.image(cloud_image, st.session_state["test_image"])



# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You entered:", my_input)