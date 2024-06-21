# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:12:15 2024

@author: ACER
"""

import pandas as pd
import streamlit as st 
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
    Bankdata.columns = [col.strip() for col in Bankdata.columns]
    Bankdata['Withdrawals']= pd.to_numeric(Bankdata['Withdrawals'], errors='coerce') 
    Bankdata['Balance']= pd.to_numeric(Bankdata['Balance'], errors='coerce')
    Bankdata['Deposits']= pd.to_numeric(Bankdata['Deposits'],  errors='coerce')
    Bankdata = Bankdata.drop('Unnamed: 5', axis=1)
    with st.expander("View All Data"):
       st.dataframe(Bankdata[['Date','Withdrawals', 'Deposits','Description']])   
    top_5_withdrawals = Bankdata.sort_values(by='Withdrawals', ascending=False).head(6)  
    top_5_withdrawals = top_5_withdrawals.reset_index(drop=True)
    top_5_wthdropt  = top_5_withdrawals.drop(index=0, axis=0, inplace=False) #drop Totals row
    top_5_deposits = Bankdata.sort_values(by='Deposits', ascending=False).head(6)
    top_5_deposits = top_5_deposits.reset_index(drop=True)
    top_5_depdropt  = top_5_deposits.drop(index=0, axis=0, inplace=False)
    with st.expander("Top 5 Withdrawls"):
       st.dataframe(top_5_wthdropt) 
    with st.expander("Top 5 Deposits"):
       st.dataframe(top_5_depdropt) 
    
    stinput = st.text_input("Enter keyword to search -")
    #
    if len(stinput) > 0:
       print('stinput-1', stinput)
       #print(np.isnan(stinput))
       dfs1 = Bankdata.loc[Bankdata['Description'].str.contains(stinput, case=False)]
       def functrunc(description):
           templst = list(description.split(' '))
           return templst[7:10]
       dfs1['Desc'] = dfs1['Description'].apply(functrunc) #adding a column for description
       dfs1w = dfs1['Withdrawals'].sum()
       dfs1d = dfs1['Deposits'].sum()
       sumdif = dfs1w - dfs1d
       st.write(f':money_with_wings: :red[WITHDRAWALS  -:  {dfs1w}]   :moneybag: :green[DEPOSITS   -:  {dfs1d}  ]')
       st.write(f':abacus: With - Dep = {sumdif}')
       with st.expander("View Transactions"):
          st.dataframe(dfs1[['Date','Desc', 'Withdrawals', 'Deposits','Description']])   
         
    else:
        print('stinput-2 ', stinput)
        dfs1d = 0
        dfs1w = 0
         
   