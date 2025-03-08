import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1-eEqWBsgVf2O-z2sjsrV5pKeU83z6qdo2szDlkLI3TU/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usercols=list(range(10)))
st.dataframe(data)
