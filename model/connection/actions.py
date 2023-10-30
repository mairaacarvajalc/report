import model.connection.conn as cn
import streamlit as st

# FindAll
findAllActions = cn.db.collection("actions")

listActions = []
for act in findAllActions.stream():
    listActions.append(act.to_dict())