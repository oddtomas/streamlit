import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import pubsub_v1
import os
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
from concurrent.futures import TimeoutError
from streamlit.scriptrunner.script_run_context import get_script_run_ctx
    
imagePrompts = {}


def list_blobs_with_prefix( ):
# def list_blobs_with_prefix( prefix ):

   
    credentials = service_account.Credentials.from_service_account_info( 
    st.secrets["gcp_service_account"] #change to secrets, this lives in the "secrets.toml" file under ".streamlit" directory
)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket("et-test-bucket")


    blobs = bucket.list_blobs()
    # blobs = bucket.list_blobs(prefix=prefix)

    print('Blobs:', blobs)


    for blob in blobs:
        
        if blob.metadata['prompt'] in imagePrompts.values():
            print("already in collection")
        elif len(imagePrompts) >= 5:
            print("collection full")
        else:
            imagePrompts.update({blob.name: blob.metadata['prompt']})
            # imagePrompts[blob.name] = blob.metadata['prompt']
            print("imagePrompts",imagePrompts)
            print("imagePrompts.values()",imagePrompts.values())
            st.write(blob.metadata['prompt']) 
            st.image(blob.download_as_bytes())


# ###########################`###############################

def subscriberz():
    credentials_path = '/Users/thatg/Desktop/streamlit_app/.streamlit/key.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    timeout = 20

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = 'projects/acto-su-1/subscriptions/bucket-updates'

# streamlit run homepage.py
    def callback(message):
        # global d

        # output = message.data.decode('utf-8')
        # d = json.loads(output)
        # print("data",message.data)
        # print(output)
        # print("message",message)
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
            list_blobs_with_prefix()
            # list_blobs_with_prefix("results/")
            streaming_pull_future.result() 
            print("this is the dictionary at the end of a loop",imagePrompts)
            print("this is the end of the subscriber")
            if len(imagePrompts) >= 5:
                streaming_pull_future.cancel()
            else:
                subscriberz()

if st.session_state["submitted"] == True:
    st.empty()
    subscriberz()
else:
    st.write("nothing to see here....YET! Go submit a prompt!")



