from cgi import test
from numpy import tri
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import pubsub_v1
import os
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
import json
import time

dictionary = {}

def list_blobs_with_prefix( prefix):
   
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket("et-test-bucket")


    blobs = bucket.list_blobs(prefix=prefix)

    print('Blobs:')

    

    for blob in blobs:
        
        if blob.metadata['prompt'] in dictionary.values():
            print("already in collection")
        else:
            dictionary.update({blob.name:blob.metadata['prompt']})
            print("dictionary",dictionary)
            st.write(blob.metadata['prompt']) 
            st.image(blob.download_as_bytes())
            

# ###########################`###############################

from concurrent.futures import TimeoutError
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
from threading import Thread

def subscriberz():
    credentials_path = '/Users/thomas.nguyen/Desktop/streamlit/.streamlit/key.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    # credentials_path = service_account.Credentials.from_service_account_info( 
    # st.secrets["gcp_service_account"])


    timeout = 20

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = 'projects/acto-su-1/subscriptions/bucket-updates'

# streamlit run homepage.py
    def callback(message):
        global d

        output = message.data.decode('utf-8')
        d = json.loads(output)
        print("callback ran")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for messages on {subscription_path}')



    with subscriber:                                                # wrap subscriber in a 'with' block to automatically call close() when done
        try:
            streaming_pull_future.result(timeout=timeout)
        # streaming_pull_future.result()                          # going without a timeout will wait & block indefinitely

        except TimeoutError:
            streaming_pull_future.cancel()
            list_blobs_with_prefix("flaskTrial/")
            streaming_pull_future.result() 
            print("this is the end of the subscriber")
            subscriberz()
if st.session_state["submitted"] == True:
    st.empty()
    subscriberz()
else:
    st.write("nothing to see here....YET! Go submit a prompt!")



