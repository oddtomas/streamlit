# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string().decode("utf-8")
    return content

bucket_name = "thomas-demo-bucket"
file_path = "prompt.txt"

content = read_file(bucket_name, file_path)

# Print results.
# for line in content.strip().split("\n"):
#     name, pet = line.split(",")
#     st.write(f"{name} has a :{pet}:")

# print(content)
st.write(content) #split this up into smaller sentences
# st.image(  st.session_state["test_image"]) #display the image from the previous page


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


st.image(cloud_image)

# if "test_image" not in st.session_state:
#     st.session_state["test_image"] = ""

# test_image = st.image(cloud_image, st.session_state["test_image"])


@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    second_text = bucket.blob(file_path).download_as_string().decode("utf-8")
    return second_text

bucket_name = "thomas-demo-bucket"
file_path = "prompt2.txt"

second_text = read_file(bucket_name, file_path)

st.write(second_text) 


@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    second_cloud_image = bucket.blob(file_path).download_as_bytes()
    return second_cloud_image

bucket_name = "thomas-demo-bucket"
file_path = "Clementine-fighting-monster.png"

second_cloud_image = read_file(bucket_name, file_path)

# Print results.
# for line in second_cloud_image.strip().split("\n"):
#     name, pet = line.split(",")
#     st.write(f"{name} has a :{pet}:")


st.image(second_cloud_image)
