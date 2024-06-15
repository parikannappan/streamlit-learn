# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:12:15 2024

@author: ACER
"""

import pandas as pd
import streamlit as st 
st.set_page_config(page_title="Bank data", page_icon="bank", layout="wide")
st.title("  :bank: Bank Report Search App")
fl = st.file_uploader(" Upload a file using 'Browse files' ", type=(["csv"]))
if fl is not None:
    bnkdata = pd.read_csv(fl, header=22)
    stinput = st.text_input("enter keyword to search(Case sensitive")
    dfs1 = bnkdata.loc[bnkdata['   Description   '].str.contains(stinput, case=False)]
    st.write(dfs1)
