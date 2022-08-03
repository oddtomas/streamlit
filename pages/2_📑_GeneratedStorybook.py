# streamlit_app.py

from numpy import test
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
# pdf test
# from fpdf import FPDF

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
#     bucket = client.bucket(bucket_name)
#     content = bucket.blob(file_path).download_as_string().decode("utf-8")
#     return content

# bucket_name = "thomas-demo-bucket"
# file_path = "prompt.txt"

# content = read_file(bucket_name, file_path)

# # Print results.
# # for line in content.strip().split("\n"):
# #     name, pet = line.split(",")
# #     st.write(f"{name} has a :{pet}:")

# # print(content)
# st.write(content) #split this up into smaller sentences
# # st.image(  st.session_state["test_image"]) #display the image from the previous page


# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
#     bucket = client.bucket(bucket_name)
#     cloud_image = bucket.blob(file_path).download_as_bytes()
#     return cloud_image

# bucket_name = "thomas-demo-bucket"
# file_path = "Clementine.png"

# cloud_image = read_file(bucket_name, file_path)

# st.image(cloud_image)




# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
#     bucket = client.bucket(bucket_name)
#     second_text = bucket.blob(file_path).download_as_string().decode("utf-8")
#     return second_text

# bucket_name = "thomas-demo-bucket"
# file_path = "prompt2.txt"

# second_text = read_file(bucket_name, file_path)

# st.write(second_text) 


# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
#     bucket = client.bucket(bucket_name)
#     second_cloud_image = bucket.blob(file_path).download_as_bytes()
#     return second_cloud_image

# bucket_name = "thomas-demo-bucket"
# file_path = "Clementine-fighting-monster.png"

# second_cloud_image = read_file(bucket_name, file_path)


# st.image(second_cloud_image)




# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
#     bucket = client.bucket(bucket_name)
#     second_text = bucket.blob(file_path).download_as_string().decode("utf-8")
#     return second_text

# bucket_name = "et-test-bucket"
# file_path = "generatedText/text_0_20220728222402.txt"

# test_text = read_file(bucket_name, file_path)

# st.write(test_text) 


#############################################################################################
bucket = client.get_bucket("et-test-bucket")
blobs = bucket.list_blobs()

collection = []

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    # Note: Client.list_blobs requires at least package version 1.17.0.

    # storage_client = client

    # blobs = storage_client.list_blobs(bucket_name)

for blob in blobs:
        if "text_" in blob.name:
            print(blob.name)
            test_text = blob.download_as_string().decode("utf-8") 
            collection.append(test_text)

# for img in blobs:

        if "image_" in blob.name:
            print(blob)
            image = blob.download_as_bytes()
            collection.append(image)
            print(blob)

list_blobs("et-test-bucket")


d = {}
d = {'image1': collection[0], 'text1': collection[10], 'image2': collection[1], 'text2': collection[11], 'image3': collection[2], 'text3': collection[12], 'image4': collection[3], 'text4': collection[13], 'image5': collection[4], 'text5': collection[14], 'image6': collection[5], 'text6': collection[15], 'image7': collection[6], 'text7': collection[16], 'image8': collection[7], 'text8': collection[17], 'image9': collection[8], 'text9': collection[18], 'image10': collection[9], 'text10': collection[19]}

if st.session_state["submitted"]: #change conditional to be if the generators are done/ send a pubsub?
# display in order of the keys
    st.write(d['text1'])
    st.image(d['image1'])
    st.write(d['text2'])
    st.image(d['image2'])
    st.write(d['text3'])
    st.image(d['image3'])
    st.write(d['text4'])
    st.image(d['image4'])
    st.write(d['text5'])
    st.image(d['image5'])
    st.write(d['text6'])
    st.image(d['image6'])
    st.write(d['text7'])
    st.image(d['image7'])
    st.write(d['text8'])
    st.image(d['image8'])
    st.write(d['text9'])
    st.image(d['image9'])
    st.write(d['text10'])
    st.image(d['image10'])
else:
    st.write("nothing to see here, submit your prompt to generate your book!")


# test print loop?
# def myprint(d):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             st.write(d[v])
#         else:
#             st.write("{0} : {1}".format(k, v))


# myprint(d)


# pdf creator
# def createPdf():
#     fpdf = FPDF()
#     fpdf.add_page()
#     fpdf.set_text_color(255, 0, 0)
#     fpdf.set_font("Arial", size=12)
#     fpdf.text(50,50, txt=d['text1'])
#     # fpdf.image(d['image1'], x=10, y=10, w=40)
#     fpdf.output("output6.pdf")

# if __name__ == '__main__':
#     createPdf()
