import streamlit as st
import model.connection.actions as act

arrayActions=list(act.listActions)


arrayCases={
    1: "VBS",
    2: "VSS",
    3: "RBI",
    4: "GBI",
    5: "WN",
    6: "NB",
    7: "ERROR"
}

arrayGoal={
    1:"Target :white_check_mark:",
    2:"Stop :x:",
    3:"BreakEven :radioactive_sign: "
}

def fnFindStr(opt):
    valSelect = [act['actionName'] for act in arrayActions if opt['actionId'] == act['actionId']]
    return valSelect[0]

def fnFindStrCase(opt):
    return arrayCases[opt]

def fnFindRbtGoal(opt):
    return arrayGoal[opt]


## ARRANCA PINTAR FORMULARIO
## Neuvos cambios

with st.form("Bitacora"):

    stbActions = st.selectbox('Actions',arrayActions,format_func=fnFindStr)
    stbCase = st.selectbox('Trade Option Case',arrayCases,format_func=fnFindStrCase)
    inpNumber = st.number_input("Lotes",min_value=100,max_value=1000,step=100)
    rbtGoal = st.radio("Goal",arrayGoal,format_func=fnFindRbtGoal)
    inpIn = st.number_input("Start",max_value=500.0)
    inpOut = st.number_input("Finish",max_value=500.0)
    inpComment = st.text_area("Comments")
    uptFile = st.file_uploader("Load Image")
    onSave = st.form_submit_button("Save")

    if onSave:
        formValues = st.session_state;

        print(formValues);
    