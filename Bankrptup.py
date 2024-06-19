# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:12:15 2024

@author: ACER
"""

import pandas as pd
import streamlit as st
import numpy as np 
st.set_page_config(page_title="Bank Statement Search", page_icon="bank", layout="wide")
st.title("  :bank: :blue[Bank Statement Search App]")
fl = st.file_uploader(" Upload a file using 'Browse files' ", type=(["csv"]))
st.button("Rerun")  
if fl is not None:
    @st.cache_data
    def load_data(fl):
        Bankdata = pd.read_csv(fl, header=22)
        return Bankdata
    Bankdata = load_data(fl)
    Bankdata['   Withdrawals ']= pd.to_numeric(Bankdata['   Withdrawals '], errors='coerce') 
    Bankdata['   Balance   ']= pd.to_numeric(Bankdata['   Balance   '], errors='coerce')
    Bankdata[' Deposits ']= pd.to_numeric(Bankdata[' Deposits '],  errors='coerce')
    Bankdata = Bankdata.drop('Unnamed: 5', axis=1)

    stinput = st.text_input("Enter keyword to search -")
    #st.write(f':money_with_wings: :red[WITHDRAWALS  -:    {dfs1w}                ]')
    #st.write(f':moneybag: :green[DEPOSITS   -:   {dfs1d}                 ]')
    if len(stinput) > 0:
       print('stinput-1', stinput)
       #print(np.isnan(stinput))
       dfs1 = Bankdata.loc[Bankdata['   Description   '].str.contains(stinput, case=False)]
       dfs1w = dfs1['   Withdrawals '].sum()
       dfs1d = dfs1[' Deposits '].sum()
       st.write(f':money_with_wings: :red[WITHDRAWALS  -:    {dfs1w}                ]')
       st.write(f':moneybag: :green[DEPOSITS   -:   {dfs1d}                 ]')
       with st.expander("View Transactions"):
          st.dataframe(dfs1)    
    else:
        print('stinput-2 ', stinput)
        dfs1d = 0
        dfs1w = 0
         
   