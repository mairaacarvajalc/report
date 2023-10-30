import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json

#key_dict = json.loads(st.secrets["keydb"])

#creds = service_account.Credentials.from_service_account_info(key_dict)

#db = firestore.Client(credentials=creds, project="trading-report")

db = firestore.Client.from_service_account_json("D:\DEVELOP\\report\\firebase_obj.json")