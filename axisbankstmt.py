# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 16:04:19 2025

@author: ACER
"""

import pandas as pd
import streamlit as st
import numpy as np
st.set_page_config(page_title="Axis Bank Statement Search", page_icon="bank", layout="wide")
#st.markdown(MobileMonneyTransfer.png, unsafe_allow_html=True)
st.title("  :bank: :red[Bank Statement Search App]")
infile = st.file_uploader(" Upload a file using 'Browse files' ", type=(["xlsx"]))
st.button("Rerun")  
if infile is not None:
    @st.cache_data
    def load_data(infile):
        Bankdata = pd.read_excel(
              infile,
               skiprows=lambda x: x in [0],  # skip these row indices
               header=2)
        return Bankdata
    Bankdata = load_data(infile)
    print(Bankdata.head())
    Bankdata1 = Bankdata.drop(columns=['Chq No','Balance','Init. Br'])
    print(Bankdata1.head())
    with st.expander("View All Data"):
           #st.dataframe(Bankdata[['Date','Withdrawals', 'Deposits','Description']])
         st.text(Bankdata1.head())
    stinput = st.text_input("Enter keyword to search -")
    #
    if len(stinput) > 0:
       print('stinput-1', stinput)
       #print(np.isnan(stinput))
       #Bankdata1 = Bankdata1.replace(["NaN", "nan", "null", "NA"], np.nan)  
       Bankdata2 = Bankdata1.dropna(subset=['Particulars'])
       print(Bankdata2.head(10))
       dfs1 = Bankdata2.loc[Bankdata2['Particulars'].str.contains(stinput, case=False)]
       def functrunc(description):
           templst = list(description.split(' '))
           return templst[7:10]
       dfs1['Desc'] = dfs1['Particulars'].apply(functrunc) #adding a column for description
       dfs1w = dfs1['Debit'].sum()
       dfs1d = dfs1['Credit'].sum()
       sumdif = dfs1w - dfs1d
       st.write(f':money_with_wings: :red[Debit  -:  {dfs1w}]   :moneybag: :green[Credit   -:  {dfs1d}  ]')
       st.write(f':abacus: With - Dep = {sumdif}')
       dfs2 = dfs1[['Tran Date','Debit', 'Credit','Particulars']]
       #-------
       
        
       with st.expander("View Transactions"):
          st.dataframe(dfs2)   
         
    else:
        print('stinput-2 ', stinput)
        dfs1d = 0
        dfs1w = 0
         