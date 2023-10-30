import streamlit as st
## ARRANCA PINTAR FORMULARIO

form = st.form("Bitacora")


inpIn = form.text_input("Action")

form.form_submit_button("Save")